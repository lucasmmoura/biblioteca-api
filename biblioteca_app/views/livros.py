from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from biblioteca_app.models.livros import Livro
from biblioteca_app.serializers.livros import LivroSerializer


class LivroListCreateView(ListCreateAPIView):

    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    permission_classes = [IsAdminUser]


class LivroDisponivelView(ListCreateAPIView):

    queryset = Livro.objects.disponiveis()
    serializer_class = LivroSerializer
    permission_classes = [IsAuthenticated]