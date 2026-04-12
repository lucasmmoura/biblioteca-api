from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from biblioteca_app.models.emprestimos import Emprestimo
from biblioteca_app.serializers.emprestimos import EmprestimoSerializer

class EmprestimoListCreateView(ListCreateAPIView):

    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    permission_classes = [IsAuthenticated]
