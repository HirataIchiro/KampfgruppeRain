# Copied from the Dash documetation sample code at https://github.com/plotly/dash-recipes/tree/master/multi-page-app
from dash import Input, Output, html, dcc
import dash_bootstrap_components as dbc
from multi_page_app.app import app

from multi_page_app.apps.app1.Pz_Ausf import choropleth_rate_zone

year_list = list(range(2002, 2019, 1))

year_rate_type = ["1_year_survival_rate", "2_year_survival_rate", "3_year_survival_rate",
                  "4_year_survival_rate", "5_year_survival_rate", "birth_rate", "death_rate"]
layout = dbc.Container(fluid=True, children=[
    html.Br(),
    html.H1('Choropleth Map'),
    html.Br(),
    html.Div(children="Please select a year (i.e: 2018)"),
    dcc.Dropdown(
        id='year_selection',
        options=[
            {'label': x, 'value': x} for x in year_list
        ],
        value="2018",
        placeholder="choose a year",
    ),

    html.Br(),
    html.Div(children="Please the long-term/short-term business survival rate from the following choice"),
    dcc.Dropdown(
        id="rate_selection",
        options=[{'label': x, 'value': x} for x in year_rate_type],
        value="1_year_survival_rate",
        placeholder="choose a type of rate year",
    ),
    dcc.Graph(id='choropleth_map')
], style={'width': 'fit-content', 'height': 'fit-content', 'padding': 20})


@app.callback(
    Output("choropleth_map", "figure"),
    Input("year_selection", "value"),
    Input("rate_selection", "value")
)
def figure_update_choropleth_map(year_selection, rate_selection):
    fig_choropleth_map = choropleth_rate_zone(int(year_selection), str(rate_selection))
    return fig_choropleth_map
