from django.urls import path
from . import views

urlpatterns = [
    path('Informations/', views.Informations, name='Informations'),
    path('EffetsIndesirables/',views.EffetIndes, name='EffetsIndes'),
    path('mapLocalisation/',views.MapLocalisation, name='map' ),
]