import numpy as np
import pandas as pd

from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go

# Traz uma instância da aplicação para este arquivo
# É desta forma que é possível adicionar callbacks a nossa aplicação
from app.server import app

# --------------------------------------
# INIT COMPONENTS
# Nesta parte vamos inicializar opções
# --------------------------------------


# --------------------------------------
# CALLBACKS 
# --------------------------------------
@app.callback(
    Output("main_graph_1", 'figure'),
    [Input('interval-component', 'n_intervals')])
def update_chart(n_intervals):
    from app import data
    
    # Selecionar dados do dataset
    # Dados do estado de santa catarina geral (por isso city.isnana())
    df = data[['date','state','place_type','deaths']]
    df = df[ df['state'] == "SC" ]
    df = df[ df['place_type'] == 'state' ]
    df['date'] = pd.to_datetime(df['date'])

    # Criar o gráfico
    fig = px.line(df, x="date", y="deaths", title='Óbitos (acumulado)')     
    
    # Retornar o gráfico
    return fig


@app.callback(
    Output("main_graph_2", 'figure'),
    [Input('interval-component', 'n_intervals')])
def update_chart(n_intervals):
    from app import data
    
    # Selecionar dados do dataset
    # Dados do estado de santa catarina geral (por isso city.isnana())
    df = data[['date','state','place_type','deaths']]
    df = df[ df['state'] == "SC" ]
    df = df[ df['place_type'] == 'state' ]
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    df['new_deaths'] = df['deaths'].diff()

    # Criar o gráfico
    fig = px.line(df, x="date", y="new_deaths", title='Óbitos (novos)')     
    
    # Retornar o gráfico
    return fig


@app.callback(
    Output("main_graph_3", 'figure'),
    [Input('interval-component', 'n_intervals')])
def update_chart(n_intervals):
    from app import data
    
    # Selecionar dados do dataset
    # Dados do estado de santa catarina geral (por isso city.isnana())
    df = data[['date','state','place_type','deaths']]
    df = df[ df['state'] == "SC" ]
    df = df[ df['place_type'] == 'state' ]
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    df['new_deaths'] = df['deaths'].diff()
    df['new_deaths_moving_avg_7'] = df['new_deaths'].rolling(7).mean()

    # Criar o gráfico
    fig = go.Figure()
    
    fig.add_trace(
        go.Scatter(
            name="Óbitos por dia",
            x=df['date'],
            y=df['new_deaths'],
            line=dict(width=0.5,dash='solid')            
        )
    )

    fig.add_trace(
        go.Scatter(
            name="Média Móvel (7d)",
            x=df['date'],
            y=df['new_deaths_moving_avg_7'],
            line=dict(color="firebrick", width=2,dash='dash')
        )
    )

    # Adicionar outras configurações de layout
    
    # Retornar o gráfico
    return fig
