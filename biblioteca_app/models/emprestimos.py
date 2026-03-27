from django.db import models
from .base import BaseModel
from .livros import Livro
from .usuarios import Usuario

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

    def __str__(self):
        return f"{self.usuario} {self.livro}"

