from django.contrib import admin
from django.urls import path, include
#importer pour le settings.DEBUG
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('produit.urls')),
    path('personnes', include('personne.urls')),
    path('commande', include('commande.urls')),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
