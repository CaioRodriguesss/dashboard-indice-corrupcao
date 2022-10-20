import pandas as pd
import plotly.express as px
import json
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc

# Leitura do arquivo "new_corruption_data" reformulado.
df = pd.read_csv("new_corruption_data")

# Series contendo valores únicos dos anos.
s_anos = df["year"].drop_duplicates().sort_values().reset_index(drop=True).copy()


# Transformando a Series s_anos em um dict.
s_anos_dict = {}
for i, k in enumerate(s_anos.__iter__()):
    s_anos_dict[f"a{i}"] = str(k)

# Series contendo valores únicos dos países.
s_paises = df["region_name"].drop_duplicates().sort_values().reset_index(drop=True).copy()

# Leitura do arquivo geo.json e transformação em um arquivo dict python.
with open("countries.geo.json") as arquivo:
    geojson = json.load(arquivo)

# Instanciando o aplicativo e fornecendo uma folha da estilos já construída (dentro da pasta assets).
app = Dash(external_stylesheets=[__name__])

# Estabelecendo a estrutura e a localização dos componentes.
app.layout = dbc.Container(
    [
        dbc.Row(
            [
            # Coluna 1
            dbc.Col(
                [
                # Texto informativo
                dbc.Row(
                    [
                        html.H4(
                            ["Dashboard Índice de Percepção de Corrupção mundial"],
                            id="ret-orno",
                            style={
                                "color":"#F2F2F2",
                                "font-weight": "bold", 
                            }
                        ),
                    html.P(
                            [
                                """
                                O Índice de Percepção da Corrupção (CPI) é um índice que classifica os países 
                                "por seus níveis percebidos de corrupção no setor público, conforme determinado 
                                por avaliações de especialistas e pesquisas de opinião". A CPI geralmente define 
                                a corrupção como um "abuso do poder confiado para ganho privado". O índice é publicado 
                                anualmente pela organização não governamental Transparência Internacional desde 1995.
                                Trecho retirado da Wikipedia.
                                """
                            ],
                            style={"color":"#F2F2F2"}
                    ),
                    html.P(
                            [
                                """
                                O índice é avaliado em uma escala de 0 a 100, sendo 100 o sentido com menores proporções
                                de corrupão e 0 o sentido com maiores proporções de corrupção.
                                """
                            ],
                            style={"color":"#F2F2F2"}
                    )
                    ], 
                    style={
                        "padding-bottom": "0px", 
                        "border-left": "#636EFA solid 1rem", 
                        "border-radius": "5px 0px 0px 0px"
                    }
                ),
                # Lista de seleção de valores
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Dropdown(
                                    id="lista-paises",
                                    options=s_paises,
                                    value="Brazil",
                                    searchable=False,
                                    clearable=False
                                )
                            ], 
                            width=12 
                        )
                    ], 
                    style={"background-color":"#262626", "margin-top":"30px"}
                ),

                # Linha que empacota os cartões.
                dbc.Row(
                    [   # Coluna contendo o primeiro cartão.
                        dbc.Col(
                            [   # Cartão com informação do melhor ano de um País e o seu índice.
                                dbc.Card(
                                    [
                                        dbc.CardHeader(
                                            id="card-melhor-momento", 
                                            style={"background-color": "#656565", "font-weight":"bold", "color":"#F2F2F2"}
                                        ),
                                        dbc.CardBody(
                                            [
                                                dbc.Row(
                                                    [
                                                        dbc.Col(
                                                            [
                                                                html.H5(["Ano"], className="card-title", style={"color":"#F2F2F2"})
                                                            ], 
                                                            md=6
                                                        ),
                                                        dbc.Col(
                                                            [
                                                                html.H5(
                                                                    id='melhor-ano', 
                                                                    className="card-text", 
                                                                    style={"color":"#0850FF", "font-weight":"bold"}
                                                                )
                                                            ], 
                                                            md=6
                                                        )
                                                    ]
                                                ),
                                                dbc.Row(
                                                    [
                                                        dbc.Col(
                                                            [
                                                                html.H5(["Índice"], className="card-title", style={"color":"#F2F2F2"})
                                                            ], 
                                                            md=6
                                                        ),
                                                        dbc.Col(
                                                            [
                                                                html.H5(
                                                                    id='melhor-indice', 
                                                                    className="card-text", 
                                                                    style={"color":"#0850FF", "font-weight":"bold"}
                                                                )
                                                            ], 
                                                            md=6
                                                        )
                                                    ]
                                                )
                                            ]
                                        )
                                    ], 
                                    style={"box-shadow": "0 4px 4px 0 rgba(0, 0, 0, 0.15), 0 4px 20px 0 rgba(0, 0, 0, 0.19)"}
                                )
                            ], 
                            md=6
                        ),

                    # Coluna contendo o segundo cartão.
                    dbc.Col(
                        [   # Cartão com informação do pior ano de um País e o seu índice.
                            dbc.Card(
                                [
                                    dbc.CardHeader(
                                        id="card-pior-momento", 
                                        style={
                                            "background-color": "#656565", 
                                            "font-weight":"bold", 
                                            "color":"#F2F2F2",
                                        }
                                    ),
                                    dbc.CardBody(
                                        [
                                            dbc.Row(
                                                [
                                                    dbc.Col(
                                                        [
                                                            html.H5(["Ano"], className="card-title", style={"color":"#F2F2F2"}),
                                                        ]
                                                    ),
                                                    dbc.Col(
                                                        [
                                                            html.H5(
                                                                id='pior-ano', 
                                                                className="card-text",
                                                                style={"color":"#F2163E", "font-weight":"bold"}
                                                            ),
                                                        ]
                                                    ),
                                                ]
                                            ),
                                            dbc.Row(
                                                [
                                                    dbc.Col(
                                                        [
                                                            html.H5(["Índice"], className="card-title", style={"color":"#F2F2F2"}),
                                                        ]
                                                    ),
                                                    dbc.Col(
                                                        [
                                                            html.H5(
                                                                id='pior-indice', 
                                                                className="card-text",
                                                                style={"color":"#F2163E", "font-weight":"bold"}
                                                            )
                                                        ]
                                                    ),
                                                ]
                                            ),
                                        ]
                                    )
                                ], 
                                style={"box-shadow": "0 4px 4px 0 rgba(0, 0, 0, 0.15), 0 4px 20px 0 rgba(0, 0, 0, 0.19)"}
                            )
                        ], 
                        md=6
                    ),
                    ], 
                    style={"margin-top":"30px", "margin-bottom":"30px"}, 
                    justify="around"
                ),
                # Gráfico de lista
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.Graph(
                                    id="line-graf" 
                                )
                            ],
                            width=12, 
                            md=12,
                        )
                    ], 
                    style={"margin-top":"30px"}
                )
                ], 
                width=6, 
                style={
                    "margin-top":"10px",
                    "margin-left":"3px",
                    "background-color":"#262626",
                    "height":"97vh",
                    "width":"48vw",
                    "border-radius": "5px 5px 5px 5px"
                }
            ),
            # Coluna 2
            dbc.Col(
                [
                    # Slider e Gráfico de mapa
                    dbc.Row(
                        [
                            html.P(
                                ["Selecione um ano:"], 
                                style={"font-size": "20px", "color": "#F2F2F2", "font-weight":"bold"}
                            ),
                            dcc.Slider(
                                id="slider-anos",
                                min=s_anos.min(),
                                max=s_anos.max(),
                                step=None,
                                marks={
                                    str(year): {
                                        "label": str(year),
                                        "style": {"color": "#F2F2F2", "font-size":"120%"}
                                    } 
                                    for year in s_anos
                                },
                                value=2021
                            )
                        ], 
                        style={"height":"10vh"}
                    ),
                    # Gráfico de mapa
                    dbc.Row(
                        [
                            dcc.Graph(
                                id="map-graf",
                                hoverData={'points': [{'customdata': ['Brazil']}]},
                            )
                        ], 
                        style={"margin-top":"5px", "height":"86vh"}
                    )     
                ], 
                width=6,
                style={
                    "margin-top":"10px", 
                    "background-color":"#262626", 
                    "height":"97vh",
                    "width":"48.5vw",
                    "border-radius": "5px 5px 5px 5px"
                }
            )
            ], 
            style={"margin-top":"3px", "margin-left":"3px", "margin-right":"3px", "margin-bottom":"3px"},
            justify="between"
        )
    ],
    fluid=True
)

# === Interatividade === #

# Atualizar o gráfico de mapa de acordo com o ano selecionado.
@app.callback(
    Output(component_id="map-graf", component_property="figure"),
    Input(component_id="slider-anos", component_property="value")
)
def graf_mapa_ano(valor_ano):
    # Plotando a figura de mapa.
    fig = px.choropleth_mapbox(
        data_frame=df[df["year"] == int(valor_ano)],
        geojson=geojson,
        color="index",
        locations="id",
        hover_data=["region_name", "year"],
        mapbox_style="carto-darkmatter",
        zoom=1,
        color_continuous_scale=px.colors.sequential.RdBu,
        opacity=0.6,
        center=dict(lat=30, lon=-30)
    )
    # Ajustando o Layout.
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="#262626",
        font=dict(color="#F2F2F2"),
        hoverlabel=dict(
            bgcolor="#404040", bordercolor="#636EFA", font=dict(color="#F2F2F2", size=16)
        )
    )
    # Atualizando as linhas.
    fig.update_traces(
        marker_line_color="#8C8C8C",
        hovertemplate="<b>%{customdata[0]}</b><br>Ano: %{customdata[1]}<br>Índice: %{z}"
    )

    return fig

# Atualizar o campo de seleção de País (Componente Dropdown) ao passar o mouse sobre os países.
@app.callback(
    Output(component_id="lista-paises", component_property="value"),
    Input(component_id="map-graf", component_property="hoverData")
)
def alter_dropdown_pais(pais_selec):
    return str(pais_selec["points"][0]["customdata"][0]).strip()

# Atualizar o gráfico de linha de acordo com o País selecionado. 
# Os textos dos cartões e do gráfico também são atualizados com a mudança do dado do País.
@app.callback(
    [   
        Output(component_id="line-graf", component_property="figure"),
        Output(component_id="melhor-ano", component_property="children"),
        Output(component_id="melhor-indice", component_property="children"),
        Output(component_id="pior-ano", component_property="children"),
        Output(component_id="pior-indice", component_property="children"),
        Output(component_id="card-melhor-momento", component_property="children"),
        Output(component_id="card-pior-momento", component_property="children")
    ],
    Input(component_id="lista-paises", component_property="value")
)
def graf_lin_ano(pais_selec):
    # Manipulando o DataFrame da maneira que precisamos dos dados.
    df_index = df.loc[(df["region_name"] == pais_selec), :]

    # Instanciando o objeto da figura.
    fig2 = px.line(
        data_frame=df_index, 
        x="year",
        y="index",
        markers=True,
        text="index",
        hover_name="region_name"
    )

    # Definindo o Layout da figura.
    fig2.update_layout(
        title=dict(
            font=dict(color="#F2F2F2", size=20),
            text=f"<b>Valor do índice ao longo dos anos - {pais_selec}</b>"
        ),
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor="#262626",
        plot_bgcolor="#262626",
        xaxis=dict(
            color="#F2F2F2",
            showline=True,
            showspikes=True,
            spikecolor="#636EFA",
            showgrid=False,    
            showticklabels=True,
            ticks="outside",
            tickfont=dict(color="#F2F2F2", size=15),
            tickmode="linear",
            tickwidth=2,
            linewidth=2,
            title=dict(text="<b>Ano</b>", font=dict(size=20))
        ),
        yaxis=dict(
            color="#F2F2F2",
            showline=True,
            showgrid=False,
            showticklabels=True,
            ticks="outside",
            tickfont=dict(color="#F2F2F2", size=15),
            tickwidth=2,
            linewidth=2,
            title=dict(text="<b>Índice</b>", font=dict(size=20))
        ),
        hoverlabel=dict(
            bgcolor="#404040", 
            bordercolor="#636EFA", 
            font=dict(color="#F2F2F2", size=16)
        )
    )

    # Ajustando a linha.
    fig2.update_traces(
        hovertemplate="<b>%{hovertext}</b><br>Ano: %{x}<br>Índice: %{text}",
        textposition="top center", 
        line_shape="spline",
        line_width=5,
        textfont=dict(color="#F2F2F2", size=12),
        marker_size=14,
        marker_color="#F2F2F2",
        marker_line=dict(width=4)
    )

    return (
        fig2,
        str(df_index["year"].get(df_index["index"].idxmax())),
        str(df_index["index"].max()),
        str(df_index["year"].get(df_index["index"].idxmin())),
        str(df_index["index"].min()),
        str(f"Melhor momento - {pais_selec}"),
        str(f"Pior momento - {pais_selec}")
    )
    
# Rodando o aplicativo.
if __name__ == "__main__":
    app.run_server(debug=True)
