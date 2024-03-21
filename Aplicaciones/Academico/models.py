from django.db import models

# Create your models here.

class Usuario(models.Model):
    PK = models.CharField(primary_key=True, max_lenght=6)
    nombre = models.CharField(max_lenght=60)
    apellido = models.CharField(max_lenght=60)

    #Comentarios para GIT
