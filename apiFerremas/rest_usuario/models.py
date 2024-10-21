from django.db import models

# Create your models here.

# Modelo para Tipo de Usuario
class TipoUsuario(models.Model):
    idTipoUsuario = models.IntegerField(primary_key=True, verbose_name='Id de Tipo de Usuario')
    nombreTipoUsuario = models.CharField(max_length=50,verbose_name="Nombre del Tipo de Usuario")

    def __str__(self):
        return self.nombreTipoUsuario


# Modelo para Usuario
class Usuario(models.Model):
    


class Vehiculo(models.Model):
    patente = models.CharField(max_length=6,primary_key=True,verbose_name='Patente')
    marca = models.CharField(max_length=20,verbose_name='Marca Vehiculo')
    modelo = models.CharField(max_length=20, null=True,blank=True,verbose_name='Modelo')
    categoria = models.ForeignKey(TipoUsuario,on_delete=models.CASCADE)

    def __str__(self):
        return self.patente
    
class Usuario(models.Model):
    username= models.CharField(max_length=50,primary_key=True,verbose_name="nombreUsuario")
    correo  = models.EmailField(max_length=100,null=False,blank=False)
    password = models.CharField(max_length=50,null=False,blank=False)
    
    def __str__(self):
        return self.username