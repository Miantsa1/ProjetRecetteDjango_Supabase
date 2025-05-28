from django.contrib import admin

from .models import Commande


@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('personne' , 'produit' , 'quantite' , 'date_commande' )

