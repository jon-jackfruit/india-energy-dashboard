from dash import html

class PageTargets:
    pageHTML = html.P("Targets page")

class PageTargets:
    # load data
    df = pd.read_csv('static/combined_data.csv')

    # Build components for app
    badge = dbc.Button(
        [
            "Notifications",
            dbc.Badge("4", color="light", text_color="primary", className="ms-1"),
        ],
        color="primary",
    )

    # build app
    app.layout = html.Div([
        html.H1(children='State of Indian utilities', style={'textAlign':'center'}),
        dbc.Container(badge, fluid=True),
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