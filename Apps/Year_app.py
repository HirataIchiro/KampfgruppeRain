# Copied from the Dash documetation sample code at https://github.com/plotly/dash-recipes/tree/master/multi-page-app
import pandas as pd
from dash import Input, Output, html, dcc
import dash_bootstrap_components as dbc
from multi_page_app.app import app

from multi_page_app.apps.app1.Pz_Ausf import line_rate_year
from pathlib import Path

csvfile = Path(__file__).parent.joinpath('data', 'cleaned_dataset.csv')
data = pd.read_csv(csvfile)
data_table = pd.DataFrame(data)
data_year_selected = data[(data['year'] >= 2002) & (data['year'] < 2003)]
city_list = pd.DataFrame(data_year_selected)

layout = dbc.Container(fluid=True, children=[
    html.Br(),
    html.H1('Business Survival rate with respect to birth year'),
    html.P(html.Li('How long can the enterprise survive since it was birth for a selected area? '),
           style={'fontSize': 25}),
    html.Br(),
    html.Div(children="Please select a region"),
    dcc.Dropdown(
        id='city_selection',
        options=[
            {'label': x, 'value': x} for x in city_list.area
        ],
        value="City of London",
        placeholder="choose a city",
    ),
    dcc.Graph(id="linear_graph")
], style={'width': 'fit-content', 'height': 'fit-content', 'padding': 20})


@app.callback(
    Output("linear_graph", "figure"),
    Input("city_selection", "value")
)
def figure_update_linear_chart(city_selection):
    linear_fig = line_rate_year(city_selection)
    return linear_fig
