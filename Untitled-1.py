#!/usr/bin/env python
# coding: utf-8

import dash
import more_itertools
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

# Load the data using pandas
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the title of the dashboard
# app.title = "Automobile Statistics Dashboard"

#---------------------------------------------------------------------------------
# Create the dropdown menu options
dropdown_options = [
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
]
# List of years 
year_list = [i for i in range(1980, 2024, 1)]
#---------------------------------------------------------------------------------------
# Create the layout of the app
app.layout = html.Div([
    # TASK 2.1 Add title to the dashboard
    html.H1(
        "Automobile Sales Statistics Dashboard",
        style={
            'textAlign': 'center',
            'color': '#503D36',
            'fontSize': '24px'
        }
    ),

    # TASK 2.2: Add two dropdown menus
    # Add the dropdown menus to the layout
    html.Div([
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id='dropdown-statistics',
            options=dropdown_options,
            placeholder='Select a report type',
            value='Select Statistics',
            style={
                'width': '80%',
                'padding': '3px',
                'fontSize': '20px',
                'textAlignLast': 'center'
            }
        )
    ]),
    
    html.Div([
        html.Label("Select Year:"),
        dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in range(1980, 2024, 1)],
            placeholder='Select-year',
            value='Select-year',
            style={
                'width': '80%',
                'padding': '3px',
                'fontSize': '20px',
                'textAlignLast': 'center'
            }
        )
    ]),

    html.Div([  # TASK 2.3: Add a division for output display
        html.Div(id='output-container', className='chart-grid', style={'display': 'flex'}),
    ])
])

# TASK 2.4: Creating Callbacks
# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='select-year', component_property='disabled'),
    Input(component_id='dropdown-statistics', component_property='value')
)
def update_input_container(selected_statistics):
    if selected_statistics == 'Yearly Statistics': 
        return False
    else: 
        return True

# Callback for plotting
@app.callback(
    Output(component_id='output-container', component_property='children'),
    [Input(component_id='dropdown-statistics', component_property='value'), 
     Input(component_id='select-year', component_property='value')]
)
def update_output_container(selected_statistics, input_year):
    if selected_statistics == 'Recession Period Statistics':
        # Filter the data for recession periods
        recession_data = data[data['Recession'] == 1]
        # Create plots for recession data
        return create_recession_charts(recession_data)

    elif selected_statistics == 'Yearly Statistics' and input_year != 'Select-year' and input_year is not None:
        # Ensure that the input_year is valid
        yearly_data = data[data['Year'] == int(input_year)]
        # Create plots for yearly data
        return create_yearly_charts(yearly_data, input_year)

    else:
        # Return an empty div or some error message if no valid year is selected
        return html.Div("Please select a valid year and statistics type.")


# TASK 2.5: Create and display graphs for Recession Report Statistics
def create_recession_charts(recession_data):
    # Plot 1: Automobile sales fluctuate over Recession Period (year-wise) using a line chart
    yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
    R_chart1 = dcc.Graph(
        figure=px.line(
            yearly_rec,
            x='Year',
            y='Automobile_Sales',
            title="Average Automobile Sales During Recession (Year-wise)"
        )
    )

    # Plot 2: Average number of vehicles sold by vehicle type (Bar chart)
    average_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
    R_chart2 = dcc.Graph(
        figure=px.bar(
            average_sales,
            x='Vehicle_Type',
            y='Automobile_Sales',
            title="Average Vehicle Sales by Vehicle Type During Recession"
        )
    )

    # Plot 3: Pie chart for total expenditure share by vehicle type during recessions
    exp_rec = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
    R_chart3 = dcc.Graph(
        figure=px.pie(
            exp_rec,
            values='Advertising_Expenditure',
            names='Vehicle_Type',
            title="Advertising Expenditure Share by Vehicle Type During Recession"
        )
    )

    # Plot 4: Effect of unemployment rate on vehicle type and sales (Bar chart)
    unemp_data = recession_data.groupby(['Unemployment_Rate', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
    R_chart4 = dcc.Graph(
        figure=px.bar(
            unemp_data,
            x='Unemployment_Rate',
            y='Automobile_Sales',
            color='Vehicle_Type',
            labels={'Unemployment_Rate': 'Unemployment Rate', 'Automobile_Sales': 'Average Automobile Sales'},
            title="Effect of Unemployment Rate on Vehicle Type and Sales"
        )
    )

    # Combine charts into two rows for layout
    return [
        html.Div(className='chart-item', children=[R_chart1, R_chart2], style={'display': 'flex', 'gap': '20px'}),
        html.Div(className='chart-item', children=[R_chart3, R_chart4], style={'display': 'flex', 'gap': '20px'})
    ]

# TASK 2.6: Create and display graphs for Yearly Report Statistics
def create_yearly_charts(yearly_data, input_year):
    # Plot 1: Yearly Automobile Sales (line chart for the whole period)
    yas = data.groupby('Year')['Automobile_Sales'].mean().reset_index()
    Y_chart1 = dcc.Graph(
        figure=px.line(
            yas,
            x='Year',
            y='Automobile_Sales',
            title="Yearly Average Automobile Sales (Whole Period)"
        )
    )

    # Plot 2: Total Monthly Automobile Sales (line chart)
    mas = yearly_data.groupby('Month')['Automobile_Sales'].sum().reset_index()
    Y_chart2 = dcc.Graph(
        figure=px.line(
            mas,
            x='Month',
            y='Automobile_Sales',
            title=f"Total Monthly Automobile Sales in {input_year}"
        )
    )

    # Plot 3: Average number of vehicles sold by vehicle type (Bar chart)
    avr_vdata = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
    Y_chart3 = dcc.Graph(
        figure=px.bar(
            avr_vdata,
            x='Vehicle_Type',
            y='Automobile_Sales',
            title=f"Average Vehicles Sold by Vehicle Type in {input_year}"
        )
    )

    # Plot 4: Total Advertisement Expenditure for each vehicle (Pie chart)
    exp_data = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
    Y_chart4 = dcc.Graph(
        figure=px.pie(
            exp_data,
            values='Advertising_Expenditure',
            names='Vehicle_Type',
            title=f"Total Advertisement Expenditure by Vehicle Type in {input_year}"
        )
    )

    # Combine charts into two rows for layout
    return [
        html.Div(className='chart-item', children=[Y_chart1, Y_chart2], style={'display': 'flex', 'gap': '20px'}),
        html.Div(className='chart-item', children=[Y_chart3, Y_chart4], style={'display': 'flex', 'gap': '20px'})
    ]

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
