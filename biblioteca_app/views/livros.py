from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from biblioteca_app.models.livros import Livro
from biblioteca_app.serializers.livros import LivroSerializer

class LivroListCreateView(ListCreateAPIView):

    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    permission_class = IsAuthenticated