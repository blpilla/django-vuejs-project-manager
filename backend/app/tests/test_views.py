import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from app.models import Cliente, Projeto, Atividade

@pytest.mark.django_db
def test_get_clientes():
    client = APIClient()
    url = reverse('cliente-list')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_get_projetos():
    client = APIClient()
    url = reverse('projeto-list')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_get_atividades():
    client = APIClient()
    url = reverse('atividade-list')
    response = client.get(url)
    assert response.status_code == 200
