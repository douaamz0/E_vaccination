from django.shortcuts import render

# Create your views here.

def Informations(request):
    return render(request,'services/informations.html',{})

def EffetIndes(request):
    return render(request,'services/effetindes.html',{})

def MapLocalisation(request):
    return render(request,'map/maplocalisation.html')