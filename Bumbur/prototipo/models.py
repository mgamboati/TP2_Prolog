from django.db import models

# Create your models here.

class consulta(models.Model):
	titulo = models.CharField(max_length = 100)
	text_bienvenida = models.CharField(max_length = 200)
	text = models.TextField()
	tiempo = models.DateTimeField()	
