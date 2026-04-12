from rest_framework import serializers
from biblioteca_app.models import Emprestimo

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = "__all__"