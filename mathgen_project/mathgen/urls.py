
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_tree/', views.get_tree, name='get_tree'),
]
