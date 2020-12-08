from rest_framework import serializers
from cadastros.models import Pessoa


class PessoaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pessoa
        fields = ['nome', 'profissao', 'date']

class PessoaCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pessoa
        fields = ['nome', 'profissao', 'endereco', 'numero', 'date']

class PessoaDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pessoa
        fields = ['id']