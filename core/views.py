from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente
from .serializers import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
	queryset = Cliente.objects.all() #mostra a lista completa dos clientes vindas do banco de dados
	serializer_class =  ClienteSerializer