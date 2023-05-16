### Import Packages ###
import dash
import dash_bootstrap_components as dbc
from whitenoise import WhiteNoise

### Dash instance ###
external_stylesheets = [dbc.themes.CYBORG]
app = dash.Dash(
        __name__,
        external_stylesheets=external_stylesheets,
        )

server = app.server

# add a static file server
server.wsgi_app=WhiteNoise(server.wsgi_app, root='static/')

