from django.db import models




class LivroManager(models.Manager):

    def disponiveis(self):
        return self.filter(disponivel = True)