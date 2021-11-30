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

class entrada(models.Model): #Nombre de clase = Nombre de la tabla
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    emoji = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    contenido = models.CharField(max_length=100)

class psicologos(models.Model): #Nombre de clase = Nombre de la tabla
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    consultorio = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=100)

class usuarios(models.Model): #Nombre de clase = Nombre de la tabla
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    problema = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    psicologo = models.ForeignKey(psicologos, on_delete=models.CASCADE)