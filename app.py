### Import Packages ###
import dash
import dash_bootstrap_components as dbc


### Dash instance ###
external_stylesheets = [dbc.themes.CYBORG]
app = dash.Dash(
        __name__,
        external_stylesheets=external_stylesheets,
        )

server = app.server

# add a static file server
#from whitenoise import WhiteNoise
#server.wsgi_app=WhiteNoise(server.wsgi_app, root='static/')


