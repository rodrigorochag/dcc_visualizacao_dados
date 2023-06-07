from django.urls import path
from . import views

# Recebe as funções do arquivo views.py


urlpatterns = [
    #path('data_visualization/', views.data_visualization, name='data_visualization'), # Chama a função members do data_visualization/views.py
    path('graficos', views.grafico_temperatura, name='graficos'), # Chama a função grafico_temperatura do data_visualization/views.py
    path('data_visualization2/', views.co2_emissions, name="data_visualization")
]