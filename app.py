from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('combined_data.csv')

app = Dash(__name__)

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

if __name__ == '__main__':
    app.run_server(debug=True)

