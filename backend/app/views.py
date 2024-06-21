from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Cliente, Projeto, Atividade
from .serializers import ClienteSerializer, ProjetoSerializer, AtividadeSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer

    @action(detail=False, methods=['get'])
    def abertos(self, request):
        projetos_abertos = Projeto.objects.filter(status='em_andamento')
        serializer = self.get_serializer(projetos_abertos, many=True)
        return Response(serializer.data)

class AtividadeViewSet(viewsets.ModelViewSet):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer
