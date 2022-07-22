from django.shortcuts import render, redirect
from .models import Jugador
from . import models

# Create your views here.

def home(request):
    jugadores = Jugador.objects.all()
    color = models.generarColor()

    for jugador in jugadores:
        actualizarDinero(jugador, color)

    actualizarApuestas()
    
    return render(request, 'gestionJugadores.html', {'jugadores': jugadores, 'color': color})

def actualizarApuestas():
    jugadores = Jugador.objects.all()
    for jugador in jugadores:
        jugador.apuesta = models.generarColor()
        jugador.save()
    return redirect('/')

def actualizarDinero(jugador, resultado):
    dineroActual = int(jugador.dinero)
    apuesta = jugador.apuesta
    
    if dineroActual == 0:
        jugador.apuestaCant = 0
        return None
    elif dineroActual <= 1000:
        monto = dineroActual
    else:
        monto = int(dineroActual*models.generarPorcentaje())

    jugador.apuestaCant = str(monto)
    jugador.dinero = str(dineroActual - monto)
    dineroActual = int(jugador.dinero)

    if apuesta==resultado and resultado=='Verde':
        jugador.dinero = str(dineroActual + monto*10)
    elif apuesta==resultado:
        jugador.dinero = str(dineroActual + monto*2)
    
    jugador.save()

def agregarJugador(request):
    id = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    dinero = request.POST['numDinero']
    apuesta = models.generarColor()
    apuestaCant = 0
    
    if dinero=='':
        jugador = Jugador.objects.create(id=id, nombre=nombre, dinero=15000, apuesta=apuesta)
    else:
        jugador = Jugador.objects.create(id=id, nombre=nombre, dinero=dinero, apuesta=apuesta)
    return redirect('/')

def eliminarJugador(request, id):
    jugador = Jugador.objects.get(id=id)
    jugador.delete()

    return redirect('/')

def edicionJugador(request, id):
    jugador = Jugador.objects.get(id=id)

    return render(request, 'editarJugador.html', {'jugador': jugador})

def editarJugador(request):
    id = request.POST['txtCodigo']
    dinero = request.POST['numDinero']

    jugador = Jugador.objects.get(id=id)

    jugador.dinero = dinero
    jugador.save()
    return redirect('/')
