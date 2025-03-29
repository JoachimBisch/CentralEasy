from django.shortcuts import render, get_object_or_404
from .models import Service
from django.utils.text import slugify

def index(request):
    # Récupérer tous les services triés par 'order'
    services = Service.objects.all().order_by('order')

    # Dictionnaire pour stocker les services catégorisés
    categorized_services = {}
    category_orders = {}

    # Ajouter chaque service à la catégorie appropriée
    for service in services:
        category = service.category
        if category not in categorized_services:
            categorized_services[category] = []
            category_orders[category] = service.category_order  # Prendre le category_order du premier service de la catégorie
        categorized_services[category].append(service)

    # Trier les catégories par category_order
    sorted_categories = sorted(categorized_services.items(), key=lambda item: category_orders[item[0]])

    return render(request, 'index.html', {'categorized_services': sorted_categories})


def detail(request, service_title):
    service = get_object_or_404(Service, title=service_title)
    return render(request, 'detail.html', {'service': service})