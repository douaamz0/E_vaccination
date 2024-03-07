from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from .forms import CitoyenForm,ReclamationForm
from .models import Citoyen,Reclamation
from django.contrib.auth.decorators import login_required
from reportlab.pdfgen import canvas
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your views here.

@receiver(post_save, sender=User)
def create_citoyen(sender, instance, created, **kwargs):
    if created:
        Citoyen.objects.create(user=instance)

def Profil(request):
    user = request.user
    nom = user.first_name
    prenom = user.last_name

    # Vérifiez si l'utilisateur a un objet Citoyen associé
    citoyen = user.citoyen

    # Vérifiez si les champs pertinents de l'instance Citoyen sont vides
    if citoyen and not (citoyen.nom and citoyen.prenom and citoyen.date_naissance and citoyen.adresse and citoyen.telephone and citoyen.cin):
        show_remplir_info = True
    else:
        show_remplir_info = False

    return render(request, 'profil/profil.html', {'nom': nom, 'prenom': prenom, 'show_remplir_info': show_remplir_info})





from django.shortcuts import get_object_or_404

@login_required
def InfoPers(request):
    # Vérifier si l'utilisateur a déjà une instance de Citoyen associée
    citoyen = get_object_or_404(Citoyen, user=request.user)

    if request.method == 'POST':
        form = CitoyenForm(request.POST, instance=citoyen)
        if form.is_valid():
            person_info = form.save(commit=False)
            person_info.nom = request.user.first_name
            person_info.prenom = request.user.last_name
            person_info.save()

            return redirect('Profil:Profil')
    else:
        form = CitoyenForm(instance=citoyen)

    return render(request, 'profil/infoPerso.html', {'form': form})



def reclamation_view(request):
    if request.method == 'POST':
        form = ReclamationForm(request.POST)
        if form.is_valid():
            reclamation = form.save(commit=False)
            citoyen = get_object_or_404(Citoyen, user=request.user)
            reclamation.citoyen = citoyen
            reclamation.save()
            return redirect('Profil:Profil')
    else:
        form = ReclamationForm()

    context = {
        'form': form
    }

    return render(request, 'profil/reclamation.html', context)



def afficher_reclamations(request):
    user = request.user
    reclamations = Reclamation.objects.filter(citoyen=user.citoyen)

    return render(request, 'profil/afficherReclamation.html', {'reclamations': reclamations})


def telecharger_passe_vaccinal(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="passe_vaccinal.pdf"'

    p = canvas.Canvas(response)

    citoyen = request.user.citoyen

    # Définir les coordonnées de départ en bas de la page
    y = 800

    # Ajouter les informations spécifiques du citoyen dans le passe vaccinal
    p.drawString(100, y, f"Nom: {citoyen.nom}")
    y -= 20
    p.drawString(100, y, f"Prénom: {citoyen.prenom}")
    y -= 20
    p.drawString(100, y, f"Date de naissance: {citoyen.date_naissance}")
    y -= 20
    p.drawString(100, y, f"Adresse: {citoyen.adresse}")
    y -= 20
    p.drawString(100, y, f"Téléphone: {citoyen.telephone}")
    y -= 20
    p.drawString(100, y, f"CIN: {citoyen.cin}")
    y -= 20
    p.drawString(100, y, f"Date vaccination 1: {citoyen.date_vaccination1}")
    y -= 20
    p.drawString(100, y, f"Date vaccination 2: {citoyen.date_vaccination2}")

    p.showPage()
    p.save()

    return response
