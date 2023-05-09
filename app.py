from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc


df = pd.read_csv('combined_data.csv')


# Initialize the app - incorporate a Dash Bootstrap theme
app = Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# Add Navbar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Page 1", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("More pages", header=True),
                dbc.DropdownMenuItem("Page 2", href="#"),
                dbc.DropdownMenuItem("Page 3", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="NavbarSimple",
    brand_href="#",
    color="primary",
    dark=True,
)

app.layout = dbc.Container([
    dbc.Row([
        navbar
    ]),
    dbc.Row([
        html.H1(children='State of Indian utilities', className="text-primary text-center fs-3")
    ]),
    dbc.Row([
        dcc.Dropdown(df.State.unique(), 'Assam', id='dropdown-selection'),
    ]),
    dbc.Row([
        dcc.Graph(id='graph-content'),
    ])
])


#app.layout = html.Div([
#    html.H1(children='State of Indian utilities', style={'textAlign':'center'}),
#    dcc.Dropdown(df.State.unique(), 'Assam', id='dropdown-selection'),
#    dcc.Graph(id='graph-content')
#])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.State==value]
    return px.line(dff, x='Year', y='Cost-Gross Input Energy (MU)')

if __name__ == '__main__':
    app.run_server(debug=True)

