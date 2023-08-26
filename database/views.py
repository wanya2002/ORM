from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from database.form import ProductForm, VersionForm
from database.models import Product, Blog, Version


def index(request):
    context = {
        'object_list': Product.objects.all()[:3],
        'title': 'Наши продукты'
    }
    return render(request, 'database/index.html', context)


class ProductsListView(ListView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('database:products')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
#    success_url = reverse_lazy('database:products')

    def get_success_url(self):
        return reverse('database:edit', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
           context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)



class ProductsDetailView(DetailView):
    model = Product


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('database:products')


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'prv', 'data', 'publish', 'count',)
    success_url = reverse_lazy('database:index')



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