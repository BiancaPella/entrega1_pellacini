from django.db import models

class ingreso(models.Model):

    nombre = models.CharField(max_length=40)
    numero = models.IntegerField()
    email = models.EmailField()

class newsletter(models.Model):

    email2 = models.EmailField()

class consulta(models.Model):

    nombre2 = models.CharField(max_length=40)
   
