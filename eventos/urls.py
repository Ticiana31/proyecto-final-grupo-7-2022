from django.urls import path
from . import views
from eventos.view import formularioContacto, contactar

urlpatterns = [
    path('inicio/', views.Inicio, name= 'inicio'),
    path('eventos_info/', views.Informacion, name= 'eventos_info'),
    path('eventos/', views.Eventos, name= 'eventos'),
    path('recursos/', views.Recursos, name= 'recursos'),
    path('contactos/', views.Contactos, name= 'contactos'),
    path('login/', views.Login, name= 'login'),
    path('register/', views.Register, name= 'register')
    path( ´formularioContacto/´, formularioContacto)
    Path (´contactar/´, contactar)
]
