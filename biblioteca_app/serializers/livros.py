from rest_framework import serializers
from biblioteca_app.models import Livro

class LivroSerializer(serializers.ModelSerializer):
    
    total_emprestimos = serializers.IntegerField(
        read_only = True,
    )


    class Meta:
        model = Livro
        fields = "__all__"

