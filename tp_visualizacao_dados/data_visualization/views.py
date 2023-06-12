from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .codigo_graficos.graficos import plot_to_html, co2_emissions, desmatamento

"""
def data_visualization(request): # envia para urls
    return HttpResponse("Hello world! Trabalho final UFMG")
"""

"""
def data_visualization(request): # Views -> urls (url_patterns)
  template = loader.get_template('home.html')
  return HttpResponse(template.render())"""


def graficos(request): # pega o grafico do arquivo codigo_graficos/graficos.py da função plot_to_html()
    graph_html = plot_to_html()
    co2_brazil = co2_emissions()
    graph_desmatamento = desmatamento()

    context = {
       'graph_temperature_brazil':graph_html,
       'graph_co2_emissions_brazil':co2_brazil,
       'graph_desmatamento_brazil':graph_desmatamento
    }

    return render(request, 'home.html', context)


def aluno(request):
    return render(request, 'aluno.html')

def fonte_dados(request):
    return render(request, 'fonte_dados.html')