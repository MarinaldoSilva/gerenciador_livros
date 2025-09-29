from .models  import Livro
from rest_framework import serializers


class LivroSerializer(serializers.ModelSerializer):

    dono = serializers.ReadOnlyField(source = 'dono.username')

    class Meta:
        model = Livro
        fields = ['id','dono','titulo','autor', 'genero', 'dt_publicacao']
        read_only_fields = ['id','dono', 'dt_publicacao']