from django.db import models

# Create your models here.
"""

class Users_list(models.Model): #Nombre de clase = Nombre de la tabla
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=10) #Despues de guardar ejecutar  python manage.py migrate y despues python manage.py makemigrations

"""