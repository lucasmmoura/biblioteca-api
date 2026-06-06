from django.db import models
from .base import BaseModel
from .livros import Livro
from .usuarios import Usuario
from django.core.exceptions import ValidationError
from biblioteca_app.managers.emprestimo_manager import EmprestimoManager
from datetime import timedelta, date

class Emprestimo(BaseModel):
    objects = EmprestimoManager()


    usuario = models.ForeignKey(
        Usuario,
        on_delete = models.CASCADE
    )

    livro = models.ForeignKey(
        Livro,
        on_delete = models.CASCADE
    )

    data_emprestimo = models.DateField(
        verbose_name = "Data do empréstimo",
        help_text = "Data do empréstimo"

    )

    data_prevista_devolucao = models.DateField(
        verbose_name = "Data prevista para devolução",
        help_text = "Quando o livro será devolvido",
        null = True,
        blank = True
    )

    data_devolucao = models.DateField(
        verbose_name = "Data de devolução",
        help_text = "Data que o livro foi devolvido",
        null = True,
        blank = True
    )

    ativo = models.BooleanField(
        verbose_name = "O empréstimo ativo?",
        help_text = "O empréstimo está ativo?",
        default = True
    )

    valor_multa = models.DecimalField(
        verbose_name = "Valor da multa",
        help_text = "Valor da multa",
        max_digits = 6,
        decimal_places = 2,
        default = 0
    )

    quantidade_renovacoes = models.PositiveIntegerField(
        verbose_name = "Quantidade de renovações",
        help_text = "Quantas vezes a obra já foi renovada",
        default = 0
    )




    def clean(self):
        #Bloqueia novo empréstimo se se livro estiver indisponível
        if not self.pk and not self.livro.disponivel:
            raise ValidationError("Livro indisponível para empréstimo")

        #Se a data prevista de devolução for menor que a data do empréstimo gera erro
        if (self.data_prevista_devolucao and self.data_prevista_devolucao < self.data_emprestimo):
            raise ValidationError(
                "Data prevista não pode ser anterior ao empréstimo"
            )

        #Erro se houver data de devolução e a data de devolução for menor do que a do empréstimo
        if self.data_devolucao and self.data_devolucao < self.data_emprestimo:
            raise ValidationError("Data de devolução não pode ser anterior da data do empréstimo")

    def save(self, *args, **kwargs):
        self.full_clean()  # roda as validações



        if not self.pk:
            self.data_prevista_devolucao = (
                self.data_emprestimo + timedelta(days = 7)
            )



        if self.data_devolucao:

            #Quantos dias atrasou
            dias_atraso = (
                self.data_devolucao - self.data_prevista_devolucao
            ).days

            #2 Reais de multa por dia atrasado
            if dias_atraso > 0:
                self.valor_multa = dias_atraso * 2

            self.ativo = False  # finaliza empréstimo
            self.livro.disponivel = True  # libera livro
        else:
            self.ativo = True  # mantém empréstimo ativo
            self.livro.disponivel = False  # prende livro

        self.livro.save()  # salva livro
        super().save(*args, **kwargs)  # salva empréstimo



    def renovar(self):
        if self.quantidade_renovacoes >= 5:
            raise ValidationError("Limite de renovações atingido")

        if not self.ativo:
            raise ValidationError("Empréstimo finalizado")

        if date.today() < self.data_prevista_devolucao:
            raise ValidationError("Só é possível renovar na data de devolução")

        self.data_prevista_devolucao += timedelta(days = 7)
        self.quantidade_renovacoes += 1
        self.save()

    def __str__(self):
        return f"{self.usuario} {self.livro}"