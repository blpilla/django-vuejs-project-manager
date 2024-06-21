import pytest
from app.models import Cliente, Projeto, Atividade

@pytest.mark.django_db
def test_cliente_creation():
    cliente = Cliente.objects.create(nome='Cliente Teste')
    assert cliente.nome == 'Cliente Teste'

@pytest.mark.django_db
def test_projeto_creation():
    cliente = Cliente.objects.create(nome='Cliente Teste')
    projeto = Projeto.objects.create(nome='Projeto Teste', cliente=cliente, status='Em Andamento')
    assert projeto.nome == 'Projeto Teste'
    assert projeto.cliente == cliente

@pytest.mark.django_db
def test_atividade_creation():
    cliente = Cliente.objects.create(nome='Cliente Teste')
    projeto = Projeto.objects.create(nome='Projeto Teste', cliente=cliente, status='Em Andamento')
    atividade = Atividade.objects.create(nome='Atividade Teste', projeto=projeto, status='Pendente')
    assert atividade.nome == 'Atividade Teste'
    assert atividade.projeto == projeto
