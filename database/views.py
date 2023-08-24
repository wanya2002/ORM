from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from database.models import Product, Blog


def index(request):
    context = {
        'object_list': Product.objects.all()[:3],
        'title': 'Наши продукты'
    }
    return render(request, 'database/index.html', context)


#def products(request):
#    context = {
#        'object_list': Product.objects.all(),
#        'title': 'Наши продукты'
#    }
#    return render(request, 'database/products.html', context)


class ProductsListView(ListView):
    model = Product


#def categories(request, pk):
#    context = {
#        'object': Product.objects.get(id=pk),
#        'title': 'Продукт'
#    }
#    return render(request, 'database/product_detail.html', context)


class ProductsDetailView(DetailView):
    model = Product


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'prv', 'data', 'publish', 'count',)
    success_url = reverse_lazy('database:index')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'prv', 'data', 'publish', 'count',)
    success_url = reverse_lazy('database:index')


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('database:list')