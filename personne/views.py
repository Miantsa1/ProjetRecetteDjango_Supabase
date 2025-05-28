from django.shortcuts import render, redirect, HttpResponse
from .models import Personne
from django.views import View

from .forms import PersonneForm
from django.contrib import messages

# Create your views here.

def index(request, *args, **kwargs):
    liste_personne = Personne.objects.all()
    context = {
        'personnes' : liste_personne,
        'nom_personne' : 'Nom de la personne',

    }
    return render(request, 'indexPersonne.html', context)


class CreatePerson(View):
    def get(self, request, *args, **kwargs):
        form = PersonneForm()
        return render(request, 'personnes/create_personne.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = PersonneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Personne enregistré avec succès')
            return redirect('personnes:indexPersonne')
        
        else:
            messages.error(request, 'Erreur lors de l\'enregistrement de la personne')
            return render(request, 'personnes/create_person.html', {'form': form})


class UpdatePersonne(View):
    def get(self, request, pk, *args, **kwargs):
        personne = Personne.objects.get(pk=pk)
        form = PersonneForm(instance=personne)
        return render(request, 'personnes/personneUpdate.html', {'form': form})
    
    def post(self, request, pk, *args, **kwargs):
        personne = Personne.objects.get(pk=pk)
        form = PersonneForm(request.POST, request.FILES, instance=personne)
        if form.is_valid():
            form.save()
            messages.success(request, 'Personne bien modifiée avec succès')
            return redirect('personnes:indexPersonne')
        else:
            messages.error(request, 'Erreur lors de la modification de la persone')
            return render(request, 'personnes/personneUpdate', {'form': form})

class DeletePersonne(View):
    def post(self, request, pk, *args, **kwargs):
        try:
            personne = Personne.objects.get(pk=pk)
            personne.delete()
            messages.success(request, 'Personne supprimée avec succès')
        except Personne.DoesNotExist:
            messages.error(request, 'Personne introuvable')
        return redirect('personne/indexPersonne')