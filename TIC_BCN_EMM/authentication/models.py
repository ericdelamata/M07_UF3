from django.db import models

# Create your models here.
from django.db import models

class Usuari(models.Model):
    # El camp 'id' es crea automàticament com a primary key
    username = models.CharField(max_length=50, unique=True) 
    password = models.CharField(max_length=128)
    nom = models.CharField(max_length=100)                   

    def __str__(self):
        return self.username