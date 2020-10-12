from rest_framework import serializers
from .models import Cliente
#forma como serão representados os dados

class ClienteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cliente
		fields = ('id','nome', 'endereco','idade')