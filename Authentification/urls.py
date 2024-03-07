from django.urls import path
from . import views

app_name='Authentification'

urlpatterns = [
    path('', views.Accueil, name='Accueil'),
    path('identification/',views.Identification,name='identification'),
    path('inscription/',views.Inscription,name='inscription'),
    path('logout/',views.Log_out,name='logout'),
]