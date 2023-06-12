from django.urls import path
from . import views

# Recebe as funções do arquivo views.py


urlpatterns = [
    #path('data_visualization/', views.data_visualization, name='data_visualization'), # Chama a função members do data_visualization/views.py
    path('', views.graficos, name='graficos') # Chama a função grafico_temperatura do data_visualization/views.py
    #path('aluno/', views.aluno, name="aluno"),
    #path('dados/', views.dados, name="dados")
]