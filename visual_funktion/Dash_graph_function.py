import pandas as pd 

import plotly.graph_objects as go
import json 

from pathlib import Path
csvfile = Path(__file__).parent.joinpath('data', 'cleaned_dataset.csv')

data = pd.read_csv(csvfile)
data_table = pd.DataFrame(data)


year_list = list(range(2002,2019,1))

year_rate_list = list(range(1,6,1))

def survival_rate_year(year,rate_year):

	text = '_year_survival_rate'
	survival_rate = '%s%s'%(rate_year,text)
	data_year_selected = data[(data['year'] >= year) & (data['year'] < year+1)]
	data_table2 = pd.DataFrame(data_year_selected['%s'%(survival_rate)])

	index = data_table2.index 
	first_index = index[0]

	max =data_table2.stack().idxmax()
	max_location = max[0] - first_index
	min =data_table2.stack().idxmin()
	min_location = min[0] - first_index
	
	colors = ['lightslategray',] * 51
	colors[min_location] = 'crimson'
	colors[max_location] = 'blue'

	bar_chart = go.Bar(x=data_year_selected['area'],y=data_year_selected['%s'%(survival_rate)],
					text = data_year_selected['%s'%(survival_rate)],#textposition = 'outside',
				    marker_color = colors)


	fig = go.Figure(bar_chart)

	fig.update_layout(
    title = "Survival Rate in "+" %s"%(year),
    xaxis_title = "Area",
    yaxis_title = "Survival Rate (%)",


)
	fig.update_layout(
		margin=dict(l=50, r=50, t=50, b=50),
		paper_bgcolor="#fff",
		title_font_family = 'Arial Black',
		title_font_size = 30,



	)
	fig.update_xaxes(title_font=dict(size=18,family='Arial Black', color='Black'))
	fig.update_yaxes(title_font=dict(size=18, family='Arial Black', color='Black'))
	#fig.show()

	return fig

def stacked_bar_rate_city(year):

	data_year_selected = data[(data['year'] >= year) & (data['year'] < year+1)]

	stacked_bar_chart = go.Figure(data = [
		go.Bar(name = 'year 5', x=data_year_selected['area'],y=data_year_selected['5_year_survival_rate']),
		go.Bar(name = 'year 4', x=data_year_selected['area'],y=data_year_selected['4_year_survival_rate']),
		go.Bar(name = 'year 3', x=data_year_selected['area'],y=data_year_selected['3_year_survival_rate']),
		go.Bar(name = 'year 2', x=data_year_selected['area'],y=data_year_selected['2_year_survival_rate']),
		go.Bar(name = 'year 1', x=data_year_selected['area'],y=data_year_selected['1_year_survival_rate']),
	])

	stacked_bar_chart.update_layout(
		barmode = 'group',
		title = " Comparison of Survival Rate as in"+" %s"%(year),
    	xaxis_title = "Area",
    	yaxis_title = "Survival Rate (%)"
		)

	stacked_bar_chart.update_layout(
		margin=dict(l=50, r=50, t=50, b=50),
		paper_bgcolor="#fff",
		title_font_family = 'Arial Black',
		title_font_size = 30 ,


	)
	stacked_bar_chart.update_xaxes(title_font=dict(size=18,family='Arial Black', color='Black'))
	stacked_bar_chart.update_yaxes(title_font=dict(size=18, family='Arial Black', color='Black'))
	#stacked_bar_chart.show()

	return stacked_bar_chart

def line_rate_year(city):

	data_area_selected = data[(data['area'] == "%s"%(city))]

	line_chart = go.Figure(data = [
		go.Scatter(name = 'year 5', x=data_area_selected['year'],y=data_area_selected['5_year_survival_rate'],
			text = data_area_selected['5_year_survival_rate']),
		go.Scatter(name = 'year 4', x=data_area_selected['year'],y=data_area_selected['4_year_survival_rate'],
			text = data_area_selected['4_year_survival_rate']),
		go.Scatter(name = 'year 3', x=data_area_selected['year'],y=data_area_selected['3_year_survival_rate'],
			text = data_area_selected['3_year_survival_rate']),
		go.Scatter(name = 'year 2', x=data_area_selected['year'],y=data_area_selected['2_year_survival_rate'],
			text = data_area_selected['2_year_survival_rate']),
		go.Scatter(name = 'year 1', x=data_area_selected['year'],y=data_area_selected['1_year_survival_rate'],
			text = data_area_selected['1_year_survival_rate']),
	])

	line_chart.update_traces(textposition = 'bottom right')

	line_chart.update_layout(
		title = " Survival Rate Of Enterprises From Different Birth Year in"+" %s"%(city),
    	xaxis_title = "Enterprises' Birth Year",
    	yaxis_title = "Survival Rate (%)",
		title_x = 0.85,
		title_y = 0.85,
		title_font_family='Arial Black',
		title_font_size=18,



		)
	line_chart.update_xaxes(title_font=dict(size=18, family='Arial Black', color='Black'))
	line_chart.update_yaxes(title_font=dict(size=18, family='Arial Black', color='Black'))

	#line_chart.show()

	return line_chart


def  choropleth_rate_zone(year,rate_choice):
	geojson_file = Path(__file__).parent.joinpath('data', 'london_boroughs.geojson')
	with open(geojson_file) as f2:

		london_map = json.load(f2)

	data_year_selected = data[(data['year'] >= year) & (data['year'] < year+1)]
	choice = "rate_choice"

	fig = go.Figure(
	data = go.Choroplethmapbox(
		geojson=london_map,
		featureidkey="properties.name",
		locations=data_year_selected['area'],
		z=data_year_selected[rate_choice],
		zauto=True,
		colorscale='spectral',
		colorbar_title = "%s"%(rate_choice),
		marker_opacity=0.4,
		marker_line_width=0.8,
		)
	)
	fig.update_layout(
		title_text = "Choropleth Map: %s for %s"%(rate_choice,year),
		mapbox_style = "carto-positron",
		mapbox_zoom=11,
		mapbox_center = {"lat":51.53,"lon":0},
		title_x=0.8,
		title_y=0.85,
		title_font_family='Arial Black',
		title_font_size=18,

	)

	# fig.show()

	return fig