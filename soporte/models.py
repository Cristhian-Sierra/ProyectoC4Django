from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL

# Create your models here.
class PersonaSoporte(models.Model):#El parametro es una clase heredada
    nombre=models.CharField(max_length=45)
    edad=models.IntegerField(null=True,blank=True)
    activo=models.BooleanField(default=True)

class PQR(models.Model):
    persona_soporte=models.ForeignKey(PersonaSoporte,on_delete=SET_NULL,null=True)
    estado=models.CharField(max_length=45)
    comentario=models.TextField(blank=True)
    creacion=models.DateField()


