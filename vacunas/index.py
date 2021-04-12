import dash
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px
import pandas as pd 
from dash.dependencies import Input,Output

df = pd.read_csv('Covid19VacunasAgrupadas.csv')

#print(df)
#print(df.vacuna_nombre.nunique())
#print(df.vacuna_nombre.unique())

app = dash.Dash(__name__)

app.layout = html.Div([
    
    html.Div([
        html.H1('Vacunados por covid'),
        html.Img(src='assets/vacuna.png')
    ], className = 'banner'),

    html.Div([
        html.Div([
            html.P('Selecciona la dosis', className = 'fix_label', style={'color':'black', 'margin-top': '2px'}),
            dcc.RadioItems(id = 'dosis-radioitems', 
                            labelStyle = {'display': 'inline-block'},
                            options = [
                                {'label' : 'Primera dosis', 'value' : 'primera_dosis_cantidad'},
                                {'label' : 'Segunda dosis', 'value' : 'segunda_dosis_cantidad'}
                            ], value = 'primera_dosis_cantidad',
                            style = {'text-aling':'center', 'color':'black'}, className = 'dcc_compon'),
        ], className = 'create_container2 five columns', style = {'margin-bottom': '20px'}),
    ], className = 'row flex-display'),

    html.Div([
        html.Div([
            dcc.Graph(id = 'my_graph', figure = {})
        ], className = 'create_container2 eight columns'),

        html.Div([
            dcc.Graph(id = 'pie_graph', figure = {})
        ], className = 'create_container2 five columns')
    ], className = 'row flex-display'),

], id='mainContainer', style={'display':'flex', 'flex-direction':'column'})

@app.callback(
    Output('my_graph', component_property='figure'),
    [Input('dosis-radioitems', component_property='value')])

def update_graph(value):

    if value == 'primera_dosis_cantidad':
        fig = px.bar(
            data_frame = df,
            x = 'jurisdiccion_nombre',
            y = 'primera_dosis_cantidad')
    else:
        fig = px.bar(
            data_frame= df,
            x = 'jurisdiccion_nombre',
            y = 'segunda_dosis_cantidad')
    return fig

@app.callback(
    Output('pie_graph', component_property='figure'),
    [Input('dosis-radioitems', component_property='value')])

def update_graph_pie(value):

    if value == 'primera_dosis_cantidad':
        fig2 = px.pie(
            data_frame = df,
            names = 'jurisdiccion_nombre',
            values = 'primera_dosis_cantidad')
    else:
        fig2 = px.pie(
            data_frame = df,
            names = 'jurisdiccion_nombre',
            values = 'segunda_dosis_cantidad'
        )
    return fig2

if __name__ == ('__main__'):
    app.run_server(debug=True)