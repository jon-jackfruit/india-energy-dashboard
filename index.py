### Import Packages ###
from dash import Dash, html, dcc, callback, Output, Input
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from whitenoise import WhiteNoise


### Import Dash Instance and Pages ###
from app import app
from pages import page_1
from pages import page_2
from pages import discoms

### Create server for Heroku to call
server = app.server
# add a static file server
server.wsgi_app=WhiteNoise(server.wsgi_app, root='static/')

### Sidebar ###
# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
sidebar = html.Div(
    [
        html.H2("India Energy Dashboard", className="display-4"),
        html.Hr(),
        html.P(
            "v0.0", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("DISCOMs", href="/discoms", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)



content = html.Div(id="page-content", style=CONTENT_STYLE)



### Set app layout to page and sidebar ###
page_container = html.Div(
    children = [
        # represents the URL bar, doesn't render anything
        dcc.Location(id="url", refresh=False),
        
        # constant sidebar
        sidebar,

        # content will be rendered in this element
        content
    ]
)


app.layout = page_container


### Index Page Layout ###
index_layout = html.Div(
    children=[
        html.H3("Home", className="display-4"),
    ]
)

### Assemble all layouts ###
app.validation_layout = html.Div(
    children = [
        page_container,
        index_layout,
        page_1.layout,
        page_2.layout,
        discoms.layout,
    ]
)

### Update Page Container ###
@app.callback(
    Output(
        component_id='page-content',
        component_property='children',
        ),
    [Input(
        component_id='url',
        component_property='pathname',
        )]
)

def display_page(pathname):
    if pathname == '/':
        return index_layout
    elif pathname == '/discoms':
        return discoms.layout
    elif pathname == '/page-2':
        return page_2.layout
    else:
        return '404'

