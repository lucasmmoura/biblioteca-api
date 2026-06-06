from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from biblioteca_app.models.livros import Livro
from biblioteca_app.serializers.livros import LivroSerializer
from django.db.models import Count


class LivroListCreateView(ListCreateAPIView):

    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    permission_classes = [IsAdminUser]


class LivroDisponivelView(ListCreateAPIView):

    queryset = Livro.objects.disponiveis()
    serializer_class = LivroSerializer
    permission_classes = [IsAuthenticated]


class LivrosMaisEmprestadosView(ListCreateAPIView):

    serializer_class = LivroSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Livro.objects.annotate(
            total_emprestimos = Count("emprestimo") #Total de emprestimos do livro
        ).order_by ("-total_emprestimos")           #Ordenar por ordem decrescente

class LivrosPorCategoriaView(ListCreateAPIView):

    serializer_class = LivroSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Retorna livros por categoria

        A categoria é recebida por parâmetro na URL

        Exemplo:
        /api/livros/categoria/?categoria=Fantasia
        """

        categoria = self.request.GET.get("categoria")

        return Livro.objects.filter(
            categoria = categoria
        )