from rest_framework import serializers
from .models import Cliente, Projeto, Atividade

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome']

class ProjetoSerializer(serializers.ModelSerializer):
    cliente_nome = serializers.ReadOnlyField(source='cliente.nome')

    class Meta:
        model = Projeto
        fields = ['id', 'nome', 'cliente', 'cliente_nome', 'status']

class AtividadeSerializer(serializers.ModelSerializer):
    projeto_nome = serializers.ReadOnlyField(source='projeto.nome')

    class Meta:
        model = Atividade
        fields = ['id', 'nome', 'projeto', 'projeto_nome', 'status']
