
from django.urls import path
from .views import index , CreateCommande, UpdateCommande, DeleteCommande

app_name = 'commandes'
urlpatterns = [
    path('', index, name='indexCommande'),
    path('create-commande/', CreateCommande.as_view(), name='create_commande'),
    path('commandeUpdate/<int:pk>', UpdateCommande.as_view(), name='commandeUpdate'),
    path('commandeDelete/<int:pk>', DeleteCommande.as_view(), name='commandeDelete'),
    

]