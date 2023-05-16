from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from whitenoise import WhiteNoise

# Setup app and server
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# add a static file server
server.wsgi_app=WhiteNoise(server.wsgi_app, root='static/')

# load data
df = pd.read_csv('static/combined_data.csv')

# build app
app.layout = html.Div([
    html.H1(children='State of Indian utilities', style={'textAlign':'center'}),
    dcc.Dropdown(df.State.unique(), 'Assam', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.State==value]
    return px.line(dff, x='Year', y='Cost-Gross Input Energy (MU)')

# start server
if __name__ == '__main__':
    app.run_server(debug=True)

