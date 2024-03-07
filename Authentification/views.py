from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.db.models import Q
from django.contrib import messages

# Create your views here.

def Accueil(request):
    return render(request,'index.html',{}) 


def Identification(request):
    if request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        user = User.objects.filter(email=email).first()
        if user:
            auth_user = authenticate(username=user.username, password=password)
            if auth_user:
                login(request, auth_user)
                request.session['is_authenticated'] = True  # Définir la variable de session
                return redirect('Profil:Profil')
            else:
                messages.error(request, "Mot de passe incorrect.")
        else:
            messages.error(request, "Email invalide.")

    # Vérifier si l'utilisateur est déjà authentifié et rediriger vers le profil
    if request.user.is_authenticated or request.session.get('is_authenticated', False):
        return redirect('Profil:Profil')

    return render(request, 'authentification/identification.html', {})


def Inscription(request):
    error=False
    message=''
    if request.method=='POST':
        nom=request.POST.get('nom',None)
        prenom=request.POST.get('prenom',None)
        email=request.POST.get('email',None)
        password1=request.POST.get('password1',None)
        password2=request.POST.get('password2',None)

        try:
            validate_email(email)
        except:
            error=True
            message="Veuillez saisir un email valid !"

        if error==False:
            if password1!=password2:
                error=True
                message="Les mots de passe ne correspondent pas ! "
        
        user=User.objects.filter(Q(email=email)).first()
        if user:
            error=True
            message="un utilisateur avec l'email {email} existe deja !"

        if error==False:
            user=User(
                first_name=prenom,
                last_name=nom,
                email=email,
                username=prenom
            )
            user.save()
            user.password=password1
            user.set_password(user.password)
            user.save()
            return redirect('Authentification:identification')
    context={
        'error':error,
        'message':message
    }
    return render(request,'authentification/inscription.html',context)

def Log_out(request):
    logout(request)
    return redirect('Authentification:identification')