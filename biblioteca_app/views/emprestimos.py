from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import ListAPIView
from biblioteca_app.models.emprestimos import Emprestimo
from biblioteca_app.serializers.emprestimos import EmprestimoSerializer

class EmprestimoListCreateView(ListCreateAPIView):

    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    permission_classes = [IsAdminUser]


class EmprestimoAtivoView(ListAPIView):

    queryset = Emprestimo.objects.ativos()
    serializer_class = EmprestimoSerializer
    permission_classes = [IsAuthenticated]

class EmprestimoAtrasadoView(ListAPIView):

    queryset = Emprestimo.objects.atrasados()
    serializer_class = EmprestimoSerializer
    permission_classes = [IsAuthenticated]

class HistoricoUsuarioView(ListAPIView):

    serializer_class = EmprestimoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        usuario_id = self.kwargs["usuario_id"]

        return Emprestimo.objects.filter(
            usuario_id = usuario_id
        )