from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


# Create your models here.


class EquipeMedicale(models.Model):
    numEquipe=models.IntegerField(primary_key=True)
    def __str__(self):
        return str(self.numEquipe)

class MembreEquipe(models.Model):
    nom=models.CharField(max_length=50)
    prenom=models.CharField(max_length=50)
    cin=models.CharField(max_length=10)
    equipe = models.ForeignKey(EquipeMedicale, on_delete=models.CASCADE ,null=True)
    def __str__(self):
        return self.nom
    


    
class Citoyen(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_naissance = models.DateField(default='2023-01-01')
    adresse = models.CharField(max_length=70)
    telephone = models.CharField(max_length=13,unique=True)
    cin = models.CharField(max_length=10,unique=True)
    date_vaccination1 = models.DateField(default='2023-01-01')
    date_vaccination2 = models.DateField(default='2023-01-01')
    equipe = models.ForeignKey(EquipeMedicale, on_delete=models.CASCADE, null=True)
    profil_complete = models.BooleanField(default=False)
    def __str__(self):
        return self.nom

    def get_telecharger_passe_vaccinal_url(self):
        return reverse('Profil:telecharger_passe_vaccinal')



class Reclamation(models.Model):
    # Champs pour les informations de la réclamation
    citoyen = models.ForeignKey(Citoyen, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100,null=False)
    date_reclamation = models.DateTimeField(null=False)
    description = models.TextField(null=False)

    # Champs pour les informations sur les effets secondaires
    symptomes = models.TextField(null=False)
    date_effets_secondaires = models.DateField(null=False)

    # Champs supplémentaires pour le suivi de la réclamation
    est_traitee = models.BooleanField(default=False)
    date_traitement = models.DateTimeField(null=True, blank=True)
    commentaire_traitement = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Réclamation de {self.nom} ({self.date_reclamation})"


