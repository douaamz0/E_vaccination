from django.urls import path
from . import views

app_name='Profil'

urlpatterns = [
    path('Profil/', views.Profil, name='Profil'),
    path('Infopers/',views.InfoPers,name='infopers'),
    path('Reclamation/',views.reclamation_view,name='reclamation'),
    path('telecharger-passe-vaccinal/', views.telecharger_passe_vaccinal, name='telecharger_passe_vaccinal'),
    path('AfficherReclamation/',views.afficher_reclamations,name='afficherReclamation'),
    
]