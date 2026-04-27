from django.db import models
from .base import BaseModel
from .livros import Livro
from .usuarios import Usuario
from django.core.exceptions import ValidationError

class Emprestimo(BaseModel):
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


    def clean(self):
        #Bloqueia novo empréstimo se se livro estiver indisponível
        if not self.pk and not self.livro.disponivel:
            raise ValidationError("Livro indisponível para empréstimo")

        #Se a data prevista de devolução for menor que a data do empréstimo gera erro
        if self.data_prevista_devolucao < self.data_emprestimo:
            raise ValidationError("Data prevista não pode ser anterior ao empréstimo")

        #Erro se houver data de devolução e a data de devolução for menor do que a do empréstimo
        if self.data_devolucao and self.data_devolucao < self.data_emprestimo:
            raise ValidationError("Data de devolução não pode ser anterior da data do empréstimo")

    def save(self, *args, **kwargs):
        self.full_clean()  # roda as validações

        if self.data_devolucao:
            self.ativo = False  # finaliza empréstimo
            self.livro.disponivel = True  # libera livro
        else:
            self.ativo = True  # mantém empréstimo ativo
            self.livro.disponivel = False  # prende livro

        self.livro.save()  # salva livro
        super().save(*args, **kwargs)  # salva empréstimo


    def __str__(self):
        return f"{self.usuario} {self.livro}"