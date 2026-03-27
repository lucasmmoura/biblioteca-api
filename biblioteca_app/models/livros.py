from django.db import models
from .base import BaseModel

class Livro(BaseModel):
    titulo = models.CharField(
        verbose_name = "Livro",
        help_text = "Nome do livro",
        max_length = 100
    )

    autor = models.CharField(
        verbose_name = "Autor",
        help_text = "Nome do autor",
        max_length = 100
    )

    categoria = models.CharField(
        verbose_name = "Categoria",
        help_text = "Romance, Terror etc..",
        max_length = 50
    )

    disponivel = models.BooleanField(
        verbose_name = "Disponível?",
        help_text = "O livro está disponível?",
        default = True
    )

    def __str__(self):
        return self.titulo