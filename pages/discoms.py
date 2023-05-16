from dash import html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

### Import Dash Instance ###
from app import app



df = pd.read_csv('static/combined_data.csv')

layout = html.Div([
    html.H1(children='State of Indian utilities', style={'textAlign':'center'}),
    dcc.Dropdown(df.State.unique(), 'Assam', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@app.callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.State==value]
    return px.line(dff, x='Year', y='Cost-Gross Input Energy (MU)')
