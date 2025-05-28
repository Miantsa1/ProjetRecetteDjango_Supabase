from django.db import models

# commande/models.py
class Commande(models.Model):
    personne = models.ForeignKey('personne.Personne', on_delete=models.CASCADE)
    produit = models.ForeignKey('produit.Produit', on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    date_commande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande de {self.produit.nom} par {self.personne.nom_personne}"
