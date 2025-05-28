from django.urls import path
from .views import index , CreatePerson, UpdatePersonne, DeletePersonne

app_name = 'personnes'
urlpatterns = [
    path('', index, name='indexPersonne'),
    path('create-personne/', CreatePerson.as_view(), name='create_personne'),
    path('personneUpdate/<int:pk>', UpdatePersonne.as_view(), name='personneUpdate'),
    path('personneDelete/<int:pk>', DeletePersonne.as_view(), name='deletePersonne' ),
    
]