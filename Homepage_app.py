# Adapted from https://dash.plotly.com/urls
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash import Input, Output

from multi_page_app.apps.app1 import Area_app
from multi_page_app.apps.app2 import Year_app
from multi_page_app.apps.app5 import Map_app


from multi_page_app.app import app


# Add the search bar code here
navbar = dbc.NavbarSimple(
    children=[
        dbc.Col(dbc.Input(type="search", placeholder='Search')),
        dbc.Col(dbc.Button("search", color="success", className='ms-2', n_clicks=0), width='auto',),
        dbc.NavItem(dbc.NavLink("Area ", href="/app1"), id="app-1-link"),
        dbc.NavItem(dbc.NavLink("Year", href="/app2"), id="app-2-link"),
        dbc.NavItem(dbc.NavLink("Map", href="/app5"), id="app-5-link"),
        # dbc.Col(dbc.Button("Login", color="Primary", className='ms-2', n_clicks=0), width='auto'),
        # dbc.Col(dbc.Button("Sign up", color="Primary", className='ms-2', n_clicks=0), width='auto'),

    ],
    brand="Business Statista",
    brand_href="/",
    color="primary",
    dark=True,

)


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])


index_layout = html.Div([
    dbc.Row([
        html.H1('Welcome to Business Statista'),
        html.Br(),
        # html.Br(),
    ], style={'textAlign': 'center', 'marginLeft': 80, 'marginRight': 80, 'width': 'auto'}),

    dbc.Row([
        html.A(" This webapp depicts the demography of the UK's business enterprise over the years and regions: "),
        html.Br(),
        html.P("(i) Business Enterprises that are still in their course of trading"),
        html.P("(ii) Establishment of new Enterprises"),
        html.P("(iii) Enterprise cease to operate"),
        html.Br(),
        html.A('To view the data or information, please click on the following link:'),
        html.Br(),

    ], style={'textAlign': 'left', 'fontSize': 30, 'marginLeft': 80, 'marginRight': 80, 'width': 'auto'}),


    dbc.Row([


        html.Li(dcc.Link('Business Survival rate with respect to area ', href='/app1')),
        html.Br(),
        html.Li(dcc.Link('Business Survival rate with respect to birth year', href="/app2")),
        html.Br(),
        html.Li(dcc.Link('Business Sustainability in according to location (Choropleth Map)', href="/app5")),

    ], style={'textAlign': 'left', 'fontSize': 30, 'marginLeft': 80, 'marginRight': 80})




], style={'width': 'fit-content', 'height': 'fit-content', 'padding': 20})


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/app1':
        return Area_app.layout
    elif pathname == '/app2':
        return Year_app.layout
    # elif pathname == '/app3':
    #     return recycle_app.layout
    elif pathname == '/app5':
        return Map_app.layout
    elif pathname == '/':
        return index_layout
    else:
        return '404 Page Not Found'


if __name__ == '__main__':
    app.run_server(debug=True)
