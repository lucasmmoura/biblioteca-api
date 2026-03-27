from django.db import models
from .base import BaseModel

class Usuario(BaseModel):
    nome = models.CharField(
        verbose_name = "Nome",
        help_text = "Nome do usuário",
        max_length = 100
    )

    email = models.EmailField(
        verbose_name = "Email",
        help_text = "Email do usuário",
        unique = True
    )

    def __str__(self):
        return self.nome