from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from biblioteca_app.models.usuarios import Usuario
from biblioteca_app.serializers.usuarios import UsuarioSerializer

class UsuarioListCreateView(ListCreateAPIView):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_class = [IsAuthenticated]