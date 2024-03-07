from django.contrib import admin
from .models import MembreEquipe,EquipeMedicale,Citoyen,Reclamation
# Register your models here.

admin.site.register(MembreEquipe)
admin.site.register(EquipeMedicale)
admin.site.register(Citoyen)
admin.site.register(Reclamation)