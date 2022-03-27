import dash_bootstrap_components as dbc
from dash import dcc, Output, Input
from dash import html

# plotly is not used in code but is imported to prevent callback error on chrome.

from plotly.validator_cache import ValidatorCache
from multi_page_app.apps.app1.Pz_Ausf import survival_rate_year
from multi_page_app.apps.app1.Pz_Ausf import stacked_bar_rate_city

from multi_page_app.app import app

# create dataset
year_list = list(range(2002, 2019, 1))
year_rate_list = list(range(1, 6, 1))


# Create the app layout using Bootstrap fluid container
layout = dbc.Container(fluid=True, children=[
    dbc.Row(
        dbc.Col(children=[html.Br(),
                          html.H1('Business survival rate with respect to area'),
                          html.P(html.Li('Find the right/best place to set-up an entity for trading activities.',
                                 style={'fontSize': 25}))
                          ]),
    ),

    html.Br(),
    html.Br(),

    dbc.Row([
        dbc.Col(children=[
            html.H4("Select the business survival rate as of year: "),
            dcc.Dropdown(id="year_selection",
                         options=[{"label": x, "value": x} for x in year_list],
                         value=2018,
                         placeholder="choose a year"),
            html.Br(),
            html.Br(),
            html.H4('Select the period of the business survive (i.e long-term/short term):'),
            dcc.Dropdown(
                id="year_rate_selection",
                options=[
                    {"label": x, "value": x} for x in year_rate_list],
                value=1,
                placeholder="choose a survival rate year"
            ),

            html.Br(),
            html.Br(),
            html.H2(''),
            dcc.Graph(id="year_und_rate_map"),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Row([
                html.H1('Longevity of the business entity in different areas'),
                html.Br(),
                html.Br(),
                html.Br(),

                html.Div(children=" Select year as of"),
                html.Br(),
                    dcc.Dropdown(id="year_selection_2", options=[{"label": x, "value": x} for x in year_list],
                                 value=2018, placeholder="choose a year"), ]),
            html.Br(),
            html.Br(),
            dcc.Graph(id="stacked_bar_rate_city"),
        ], style={"height": 2500, "width": 1200}, )
    ])
], style={'width': 'fit-content', 'height': 'fit-content', 'padding': 20, })


# Create the callbacks


@app.callback(
        Output("year_und_rate_map", "figure"),
        Input("year_selection", "value"),
        Input("year_rate_selection", "value")
)
def figure_update_bar_chart(year_selection, year_rate_selection):

    fig = survival_rate_year(year_selection, year_rate_selection)

    return fig


@app.callback(
    Output("stacked_bar_rate_city", "figure"),
    Input("year_selection_2", "value"),
)
def figure_update_bar_chart(year_selection_2):
    fig2 = stacked_bar_rate_city(year_selection_2)
    return fig2
