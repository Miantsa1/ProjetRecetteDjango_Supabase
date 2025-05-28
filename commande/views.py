from django.shortcuts import render, redirect , HttpResponse
from .models import Commande
from django.views import View
from .forms import CommandeForm
from django.contrib import messages

def index(request, *args, **kwargs):
    liste_commande = Commande.objects.all()
    context = {
        'commandes' : liste_commande     
    }
    return render(request, 'indexCommande.html', context)

class CreateCommande(View):
    def get(self, request, *args, **kwargs):
        form = CommandeForm()
        return render(request, 'commandes/create_commande.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Commande enregistrée avec succès')
            return redirect('commandes:indexCommande')
        
        else:
            messages.error(request, 'Erreur lors de l\'enregistrement de la commande')
            return render(request,'commande/create_commande.html', {'form': form})

class UpdateCommande(View):
    def get(self, request, pk, *args, **kwargs):
        commande = Commande.objects.get(pk=pk)
        form = CommandeForm(instance=commande)
        return render(request, 'commandes/commandeUpdate.html' , {'form': form})

    def post(self, request, pk, *args, **kwargs):
        commande = Commande.objects.get(pk=pk)
        form = CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            messages.success(request,'Commande bien enregistrée avec succès')
            return redirect('commandes:indexCommande')
        else:
            messages.error(request, 'Erreur lors de l\'enregistrement du commande')
            return render(request, 'commandes/commandeUpdate', {'form':form})

class DeleteCommande(View):
    def post(self, request, pk, *args, **kwargs):
        try:
            commande = Commande.objects.get(pk=pk)
            commande.delete()
            messages.success(request, 'Commande supprimée avec succès')
        except Commande.DoesNotExist:
            messages.error(request, 'Commande introuvable')
        return redirect('commandes:indexCommande')

