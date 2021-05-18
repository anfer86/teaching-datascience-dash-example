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
    
    return None