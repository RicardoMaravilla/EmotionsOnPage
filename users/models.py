from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""

class Users_list(models.Model): #Nombre de clase = Nombre de la tabla
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=10) #Despues de guardar ejecutar  python manage.py migrate y despues python manage.py makemigrations

"""
class psicologos_user(models.Model): #Nombre de clase = Nombre de la tabla
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10)
    titulo = models.CharField(max_length=50)
    consultorio = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    last_login = models.DateTimeField(auto_now=True)

class usuarios_user(models.Model): #Nombre de clase = Nombre de la tabla
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=60)
    email = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10)
    problema = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    psicologo = models.ForeignKey(psicologos_user, on_delete=models.CASCADE, null=True)
    last_login = models.DateTimeField(auto_now=True)


class entrada_user(models.Model): #Nombre de clase = Nombre de la tabla
    username = models.ForeignKey(usuarios_user, on_delete=models.CASCADE ,null=True)
    emoji = models.CharField(max_length=50, null=True)
    fecha = models.DateTimeField(null=True)
    contenido = models.CharField(max_length=100, null=True)