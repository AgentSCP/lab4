from django.urls import path, include
from .views import index, add, edit, delete

urlpatterns = [
    path('', index, name='index'),
    path('', add, name='add'),
    path('', edit, name='edit'),
    path('', delete, name='delete'),
]