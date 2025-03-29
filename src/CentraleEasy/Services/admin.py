
# Register your models here.
from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    # Personnalisez l'affichage de votre modèle ici si nécessaire
    list_display = ('title', 'category', 'order', 'category_order')
    list_editable = ('order', 'category_order')

# Enregistrez votre modèle dans l'interface d'administration
admin.site.register(Service, ServiceAdmin)