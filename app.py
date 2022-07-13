
import dash 
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

external_script = ["https://tailwindcss.com/", {"src": "https://cdn.tailwindcss.com"}]

app = dash.Dash(
    __name__,
    external_scripts=external_script,
)
app.scripts.config.serve_locally = True


df = pd.read_csv('Covid19VacunasAgrupadas.csv')

app.layout = html.Div([
    
    html.Div([
        html.H1('VACUNADOS POR COVID'),
    ], className = 'flex flex-nowrap bg-gray-700 text-3xl p-7 tracking-wider text-gray-50 font-bold lg:text-left text-center'),

    html.Div([
        html.Div([
            html.P('Selecciona la dosis', className = 'text-gray-500'),
            dcc.RadioItems(id = 'dosis-radioitems', 
                            options = [
                                {'label' : 'Primera dosis', 'value' : 'primera_dosis_cantidad' },
                                {'label' : 'Segunda dosis', 'value' : 'segunda_dosis_cantidad' }
                            ], value = 'primera_dosis_cantidad',
                            className = 'flex flex-nowrap space-x-5 items-center text-gray-500'),
        ], className = 'py-2 px-5 flex flex-nowrap text-sm space-x-5 justify-end items-center'),
        html.Div([
            html.A('GRÁFICO BARRAS', className = 'py-3 px-5 bg-gray-600 hover:bg-gray-500 flex flex-1 lg:flex-auto justify-center', href = "#my_graph"),
            html.A('GRÁFICO CIRCULAR', className = 'py-3 px-5 bg-gray-600 hover:bg-gray-500 flex flex-1 lg:flex-auto justify-center', href = "#pie_graph"),
        ], className = 'flex flex-nowrap text-sm text-white font-semibold divide-x divide-gray-700'),
    ], className = 'flex lg:flex-nowrap lg:flex-row flex-col justify-between bg-gray-100'),

    html.Div([
        html.Div([
            html.P('GRÁFICO BARRAS REGIONES ARGENTINA', className = 'text-gray-600 font-bold text-xl'),
            dcc.Graph(id = 'my_graph', figure = {})
        ], className = 'lg:w-[70vw] w-[90vw] mx-auto p-5 lg:p-10 bg-white rounded-lg my-10 shadow-md'),

        html.Div([
            html.P('GRÁFICO CIRCULAR REGIONES ARGENTINA', className = 'text-gray-600 font-bold text-xl'),
            dcc.Graph(id = 'pie_graph', figure = {})
        ], className = 'lg:w-[70vw] w-[90vw] mx-auto p-5 lg:p-10 bg-white rounded-lg my-10 shadow-md')
    ], className = ''),

], id='mainContainer', className = 'bg-gray-50')

#Callbacks para interacción
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