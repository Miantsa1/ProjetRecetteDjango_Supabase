from django.db import models

# Create your models here.

class Personne(models.Model):
    nom_personne = models.CharField(max_length=100)
    prenom_personne = models.CharField(max_length=150)
    telephone = models.CharField(max_length=12)
    image_personne = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.nom_personne
    
    def get_image_url(self):
        if self.image_personne:
            return self.image_personne.url 
        return None