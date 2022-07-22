from django.db import models
import random

random.seed(2)

# Create your models here.

class Jugador(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=100)
    dinero = models.CharField(max_length=20)
    apuesta = models.CharField(max_length=20)
    apuestaCant = models.CharField(max_length=20)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.dinero)

def generarColor():
    n = random.random()
    if n<0.01:
        color = 'Verde'
    elif n<0.505:
        color = 'Rojo'
    else:
        color = 'Negro'
    return color

def generarPorcentaje():
    return random.random()*(0.08) + 0.11

