from django.shortcuts import render

from database.models import Category, Product


def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Наши продукты'
    }
    return render(request, 'database/index.html', context)

def categories(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Наши продукты'
    }
    return render(request, 'database/categories.html', context)

