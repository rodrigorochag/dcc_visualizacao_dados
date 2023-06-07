from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .codigo_graficos.graficos import plot_to_html, co2_emissions, plot_to_html2

"""
def data_visualization(request): # envia para urls
    return HttpResponse("Hello world! Trabalho final UFMG")
"""


def data_visualization(request): # Views -> urls (url_patterns)
  template = loader.get_template('home.html')
  return HttpResponse(template.render())


def grafico_temperatura(request): # pega o grafico do arquivo codigo_graficos/graficos.py da função plot_to_html()
    graph_html = plot_to_html()
    co2_brazil = co2_emissions()

    context = {
       'graph_temperature_brazil':graph_html,
       'graph_co2_emissions_brazil':co2_brazil
    }

    return render(request, 'home.html', context)



# Create your views here.
