from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('agregarJugador/', views.agregarJugador),
    path('eliminarJugador/<id>', views.eliminarJugador),
    path('edicionJugador/<id>', views.edicionJugador),
    path('editarJugador/', views.editarJugador)
]