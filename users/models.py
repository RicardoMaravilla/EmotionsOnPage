from django.db import models

# Create your models here.

class users_list(models.Model): #Nombre de clase = Nombre de la tabla
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=10) #Despues de guardar ejecutar  python manage.py migrations y despues python manage.py makemigrations