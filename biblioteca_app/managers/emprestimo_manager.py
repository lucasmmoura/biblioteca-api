from django.db import models
from django.utils.timezone import now



class EmprestimoManager(models.Manager):
    def ativos(self):
        return self.filter(
            ativo = True
        )

    def atrasados(self):

        emprestimos = self.filter(ativo = True)

        atrasados = []

        for emprestimo in emprestimos:
            if emprestimo.data_prevista_devolucao < now().date():
                atrasados.append(emprestimo)

        return atrasados