from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Em Andamento', 'Em Andamento'),
        ('Concluída', 'Concluída'),
    ]

    nome = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, related_name='projetos', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente')

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Em Andamento', 'Em Andamento'),
        ('Concluída', 'Concluída'),
    ]

    nome = models.CharField(max_length=100)
    projeto = models.ForeignKey(Projeto, related_name='atividades', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pendente')

    def __str__(self):
        return self.nome
