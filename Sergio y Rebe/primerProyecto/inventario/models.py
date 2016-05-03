from django.db import models

# Create your models here.
class Cafe(models.Model):
	Nombre = models.CharField(max_length=100)
	Stock = models.CharField(max_length=100)
	Descripcion = models.TextField()	


