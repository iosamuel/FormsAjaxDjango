from django.db import models

class Datos(models.Model):
	nombre = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)
	edad = models.IntegerField()
	imagen = models.ImageField(upload_to='images')