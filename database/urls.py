from django.urls import path

from database.apps import DatabaseConfig
from database.views import index, ProductsListView, ProductsDetailView, \
    BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, \
    ProductCreateView, BlogDeleteView, ProductDeleteView, ProductUpdateView

app_name = DatabaseConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/categories/', ProductsDetailView.as_view(), name='categories'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('delete/<int:pk>', ProductDeleteView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='create_prod'),
    path('edit/<int:pk>', ProductUpdateView.as_view(), name='edit_pr'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('list/', BlogListView.as_view(), name='list'),
    path('view/<int:pk>', BlogDetailView.as_view(), name='view'),
    path('edit/<int:pk>', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete'),
]