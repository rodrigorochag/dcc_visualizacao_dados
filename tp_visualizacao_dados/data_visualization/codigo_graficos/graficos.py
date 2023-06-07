import plotly.graph_objects as go
from django.shortcuts import render
import plotly.offline as opy
import plotly.graph_objs as go

import plotly.graph_objs as go
from plotly.offline import plot

import plotly.graph_objects as go

def plot_series_temperatura():
    # Dados fornecidos
    years = list(range(1961, 2023))
    temperatures = [0.167, -0.184, 0.158, -0.213, -0.075, 0.044, 0.073, -0.409, 0.331, 0.13, -0.134, 0.114, 0.443, -0.179,
                -0.14, -0.185, 0.252, 0.03, 0.017, 0.313, 0.191, 0.277, 0.471, 0.294, 0.092, 0.285, 0.722, 0.461, 0.13,
                0.435, 0.468, 0.403, 0.495, 0.608, 0.799, 0.504, 0.671, 1.234, 0.523, 0.495, 0.746, 1.052, 0.927, 0.768,
                1.085, 0.77, 0.969, 0.731, 0.969, 1.112, 0.814, 1.023, 0.922, 1.153, 1.516, 1.457, 1.363, 1.148, 1.517,
                1.477, 1.154, 0.926]

    # Criar o gráfico interativo
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=temperatures, mode='lines+markers'))

    # Configurar o layout do gráfico
    fig.update_layout(
        title='Mudança de temperatura no Brasil',
        xaxis=dict(title='Ano'),
        yaxis=dict(title='Mudança de temperatura (°C)')
    )

    # Exibir o gráfico interativo
    fig.show()
    

    div = opy.plot(fig, auto_open=False, output_type='div')

    return div

def plot_to_html():
    # Dados fornecidos
    years = list(range(1961, 2023))
    temperatures = [0.167, -0.184, 0.158, -0.213, -0.075, 0.044, 0.073, -0.409, 0.331, 0.13, -0.134, 0.114, 0.443, -0.179,
                -0.14, -0.185, 0.252, 0.03, 0.017, 0.313, 0.191, 0.277, 0.471, 0.294, 0.092, 0.285, 0.722, 0.461, 0.13,
                0.435, 0.468, 0.403, 0.495, 0.608, 0.799, 0.504, 0.671, 1.234, 0.523, 0.495, 0.746, 1.052, 0.927, 0.768,
                1.085, 0.77, 0.969, 0.731, 0.969, 1.112, 0.814, 1.023, 0.922, 1.153, 1.516, 1.457, 1.363, 1.148, 1.517,
                1.477, 1.154, 0.926]

    # Criar o gráfico interativo
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=temperatures, mode='lines+markers'))

    # Configurar o layout do gráfico
    fig.update_layout(
        title='Mudança de temperatura no Brasil',
        xaxis=dict(title='Ano'),
        yaxis=dict(title='Mudança de temperatura (°C)')
    )

    # Converter o gráfico em HTML
    div = plot(fig, output_type='div')

    return div



def co2_emissions():  

    # Dados de emissão de CO2
    years = list(range(1990, 2022))
    emissions = [1.31313162278407, 1.3400291104962, 1.33331845207455, 1.35861090138514, 1.38213969207396, 1.47560355931892,
                1.58045379755498, 1.6691806384565, 1.6989442995386, 1.73476944842688, 1.78349954728882, 1.79211171672668,
                1.76065069014316, 1.7018519889237, 1.77844124428615, 1.77566238713021, 1.77747742696957, 1.847975735626,
                1.93921475496659, 1.79932762776072, 2.02660515963729, 2.11067771312325, 2.27141718351636,
                2.41344604124948, 2.51459146813631, 2.36536013363926, 2.16125936406967, 2.18937093870573,
                2.0649751983417, 2.05067522030747]

    # Criar figura Plotly
    #fig = go.Figure()
    fig = go.Figure(data=go.Scatter(x=years, y=emissions, mode='markers+lines'))

    # Configurar layout do gráfico
    fig.update_layout(
        title='Emissões de CO2 no Brasil 1995 a 2020',
        xaxis_title='Ano',
        yaxis_title='Emissões de CO2',
        hovermode='closest'
    )

    # Adicionar interação ao passar o mouse sobre os pontos
    fig.update_traces(hovertemplate='Ano: %{x}<br>Emissões de CO2: %{y}')

    # Exibir gráfico interativo
    #fig.show()

    div = plot(fig, output_type='div')
    return div




def plot_to_html2():
    # Dados fornecidos
    years = list(range(1961, 2023))
    temperatures = [0.167, -0.184, 0.158, -0.213, -0.075, 0.044, 0.073, -0.409, 0.331, 0.13, -0.134, 0.114, 0.443, -0.179,
                -0.14, -0.185, 0.252, 0.03, 0.017, 0.313, 0.191, 0.277, 0.471, 0.294, 0.092, 0.285, 0.722, 0.461, 0.13,
                0.435, 0.468, 0.403, 0.495, 0.608, 0.799, 0.504, 0.671, 1.234, 0.523, 0.495, 0.746, 1.052, 0.927, 0.768,
                1.085, 0.77, 0.969, 0.731, 0.969, 1.112, 0.814, 1.023, 0.922, 1.153, 1.516, 1.457, 1.363, 1.148, 1.517,
                1.477, 1.154, 0.926]

    # Criar o gráfico interativo
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=temperatures, mode='lines+markers'))

    # Configurar o layout do gráfico
    fig.update_layout(
        title='Mudança de temperatura no Brkjhihkhkjhuiasil',
        xaxis=dict(title='Ano'),
        yaxis=dict(title='Mudança de temperatura (°C)')
    )

    # Converter o gráfico em HTML
    div = plot(fig, output_type='div')

    return div
