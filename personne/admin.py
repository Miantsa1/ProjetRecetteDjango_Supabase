from django.contrib import admin


# enregistrer les tables
from .models import Personne

#admin.site.register(Produit) #ce n'est pas encore sous forme de tableau

#Pour qu'il s'affiche en tableau

@admin.register(Personne) #mettre un decorateur
class PersonneAdmin(admin.ModelAdmin):
    list_display = ('nom_personne' , 'prenom_personne' , 'telephone' , 'image_personne' )

# Register your models here.
