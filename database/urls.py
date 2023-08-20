from django.urls import path

from database.apps import DatabaseConfig
from database.views import index, categories

app_name = DatabaseConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', categories, name='categories'),
]