from rest_framework import serializers
from .models import PersonaSoporte,PQR

class PersonaSoporteSerializer(serializers.ModelSerializer):
    class Meta:
        models=PersonaSoporte
        fields='__all__'#Trae todos los campos del modelo

class PQRSerializer(serializers.ModelSerializer):
    class Meta:
        models=PQR
        fields=['persona_soporte','estado','comentario']

