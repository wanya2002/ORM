from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

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

    def form_valid(self, form):
        if form.is_valid():
            new_pub = form.save()
            new_pub.slug = slugify(new_pub.title)
            new_pub.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'prv', 'data', 'publish', 'count',)
#    success_url = reverse_lazy('database:index')

    def form_valid(self, form):
        if form.is_valid():
            new_pub = form.save()
            new_pub.slug = slugify(new_pub.title)
            new_pub.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('database:view', args=[self.kwargs.get('pk')])



class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(publish=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count +=1
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('database:list')