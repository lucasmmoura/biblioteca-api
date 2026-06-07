from django.test import TestCase
from biblioteca_app.models import Livro, Usuario, Emprestimo
from datetime import date, timedelta




class EmprestimoTestCase(TestCase):

    def test_data_prevista_automatica(self):

        usuario = Usuario.objects.create(
            nome = "Teste"
        )

        livro = Livro.objects.create(
            titulo = "Duna",
            autor = "Frank Herbert",
            categoria = "Ficção Científica"
        )

        emprestimo = Emprestimo.objects.create(
            usuario = usuario,
            livro = livro,
            data_emprestimo = date.today()
        )

        self.assertEqual(
            emprestimo.data_prevista_devolucao,
            date.today() + timedelta(days = 7)
        )



    def test_nao_empresta_livro_indisponivel(self):
        usuario = Usuario.objects.create(
            nome = "Teste"
        )

        livro = Livro.objects.create(
            titulo = "Duna",
            autor = "Frank Herbert",
            categoria = "Ficção Científica",
            disponivel = False
        )

        with self.assertRaises(Exception):
            Emprestimo.objects.create(
                usuario = usuario,
                livro = livro,
                data_emprestimo = date.today()
            )

    def test_limite_renovacoes(self):
        usuario = Usuario.objects.create(
            nome = "Teste"
        )

        livro = Livro.objects.create(
            titulo = "Duna",
            autor = "Frank Herbert",
            categoria = "Ficção Científica"
        )

        emprestimo = Emprestimo.objects.create(
            usuario = usuario,
            livro = livro,
            data_emprestimo = date.today() - timedelta(days = 50)
        )

        emprestimo.quantidade_renovacoes = 5

        with self.assertRaises(Exception):
            emprestimo.renovar()


    def test_calcula_multa_por_atraso(self):

        usuario = Usuario.objects.create(
            nome="Teste"
        )

        livro = Livro.objects.create(
            titulo="Duna",
            autor="Frank Herbert",
            categoria="Ficção Científica"
        )

        emprestimo = Emprestimo.objects.create(
            usuario = usuario,
            livro = livro,
            data_emprestimo = date.today() - timedelta(days = 10)
        )

        emprestimo.data_devolucao = (
            emprestimo.data_prevista_devolucao + timedelta(days = 3)
        )

        emprestimo.save()

        self.assertEqual(
            emprestimo.valor_multa,
            6
        )