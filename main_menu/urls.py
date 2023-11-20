from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_menu, name='main_menu'),
    path('get_graph_humidity/', views.get_graph_humidity, name='get_graph_humidity'),
    path('get_graph_nutrients/', views.get_graph_nutrients, name='get_graph_nutrients'),
    path('get_graph_temperature/', views.get_graph_temperature, name='get_graph_temperature'),
    path('get_graph_phosphorus/', views.get_graph_phosphorus, name='get_graph_phosphorus'),
    path('get_graph_pie/', views.get_graph_pie, name='get_graph_pie'),
    path('get_graph_large/', views.get_graph_large, name='get_graph_large')
]