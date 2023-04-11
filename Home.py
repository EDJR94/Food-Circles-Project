#==========================================================
#Importação das Bibliotecas
#==========================================================
import pandas as pd
import numpy as np
import inflection
import plotly.express as px
import folium
import streamlit as st
from folium.plugins import MarkerCluster
from PIL import Image
from streamlit_folium import folium_static

st.set_page_config(page_title='Home', page_icon='🏠', layout='wide')

#Importação do arquivo
df = pd.read_csv('zomato.csv')

#==========================================================
#Funções
#==========================================================
#Nome dos países com base no código
countries = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zeland",
162: "Philippines",
166: "Qatar",
184: "Singapure",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America",
}
#Função para substituir o código dos países pelo nome dos países no Dataframe
def country_name(country_id):
  return countries[country_id]

#Função para substituir o número do price_range pelo nome dos price_range no Dataframe
def create_price_type(price_range):
  if price_range == 1:
    return "cheap"
  elif price_range == 2:
    return "normal"
  elif price_range == 3:
    return "expensive"
  else:
    return "gourmet" 

#Código das Cores
colors = {
"3F7E00": "darkgreen",
"5BA829": "green",
"9ACD32": "lightgreen",
"CDD614": "orange",
"FFBA00": "red",
"CBCBC8": "darkred",
"FF7800": "darkred",
}

#Função para substituir o código das cores pelo nome das cores no Dataframe
def color_name(color_code):
  return colors[color_code]

#Código das Moedas
codigos_moeda = {
 'Botswana Pula(P)': 'BWP',   
 'Brazilian Real(R$)': 'BRL',
 'Dollar($)': 'USD',
 'Emirati Diram(AED)': 'AED',
 'Indian Rupees(Rs.)': 'INR',
 'Indonesian Rupiah(IDR)': 'IDR',
 'NewZealand($)': 'NZD',
 'Pounds(£)': 'GBP',
 'Qatari Rial(QR)': 'QAR',
 'Rand(R)': 'ZAR',
 'Sri Lankan Rupee(LKR)': 'LKR',
 'Turkish Lira(TL)': 'TRY', 
}

#Função para substituir o nome das moedas pelo código das moedas no Dataframe
def renomear_moedas(moeda):
  return codigos_moeda[moeda]

#Taxa de conversão das moedas para dólar
taxa_dolar =  {
 'BWP': 13.0675,
 'BRL': 4.8828,
 'USD': 1.0000,
 'AED': 3.6607, 
 'INR': 81.6273, 
 'IDR': 14817.5759, 
 'NZD': 1.5897, 
 'GBP': 0.8010, 
 'QAR': 3.64,
 'ZAR': 18.0567, 
 'LKR': 305.9658, 
 'TRY': 19.1605,  
}

#Função para substituir o valor da coluna average_cost_for_two pelo valor convertido em dólar
def moeda_dolar(valor,moeda):
  return valor/taxa_dolar[moeda]

#Função para renomear as colunas
#Deixar todos os nomes com letra minúscula e substituir os espaços por "_"
def rename_columns(dataframe):
  df = dataframe.copy()
  title = lambda x: inflection.titleize(x)
  snakecase = lambda x: inflection.underscore(x)
  spaces = lambda x: x.replace(" ", "")
  cols_old = list(df.columns)
  cols_old = list(map(title, cols_old))
  cols_old = list(map(spaces, cols_old))
  cols_new = list(map(snakecase, cols_old))
  df.columns = cols_new
  return df

#Função para retirar Outliers da coluna average_cost_for_two baseado na mediana
def mediana_pais(df,pais):
  df2 = df.copy()
  filtro_pais = df2['country_code'] == pais
  mediana = df2.loc[filtro_pais,['average_cost_for_two']].median().values[0]
  filtro_mediana = df2['average_cost_for_two'] > 20*mediana
  df2.loc[(filtro_pais) & (filtro_mediana),'average_cost_for_two'] = mediana
  return df2   

#Função que encontra restaurante com maior ou menor nota baseado na culinária selecionada
def restaurant_by_cuisine(cuisine,min_max):
  filtro_cuisine_american = df2['cuisines'] == cuisine
  df2_filtrado = (df2.loc[filtro_cuisine_american,['restaurant_name','aggregate_rating','restaurant_id']]
              .groupby(['restaurant_name','restaurant_id'])
              .mean()
              .reset_index()
              .sort_values(by='aggregate_rating',ascending=min_max))
  df2_apenas_melhores_medias = df2_filtrado['aggregate_rating'] == df2_filtrado.iloc[0,2]
  df2_desempate = df2_filtrado.loc[df2_apenas_melhores_medias,:].sort_values(by='restaurant_id',ascending=True)
  if min_max:
    return print(f"O restaurante com a menor nota média que possui apenas o tipo de culinária {cuisine} é {df2_desempate.iloc[0,0]} com a média de {df2_desempate.iloc[0,2]}")
  else:
    return print(f"O restaurante com a maior nota média que possui apenas o tipo de culinária {cuisine} é {df2_desempate.iloc[0,0]} com a média de {df2_desempate.iloc[0,2]}")  

#==========================================================
#Limpeza de Dados
#==========================================================
df1 = df.copy()

#Retirando linhas duplicadas
df1 = df1.drop_duplicates()

#Retirando NaN
df1 = df1.dropna()

#Transformando Código dos países em países
df1['Country Code'] = df1['Country Code'].apply(country_name)

#Price Range das comidas
df1['Price range'] = df1['Price range'].apply(create_price_type)

#Mudar código de cores
df1['Rating color'] = df1['Rating color'].apply(color_name)

#Mudar código das moedas
df1['Currency'] = df1['Currency'].apply(renomear_moedas)

#Mudar nome colunas
df1 = df1.reset_index(drop=True)
df2 = df1.copy()
df2 = rename_columns(df1)

#Deixar apenas um nome na culinária
df2['cuisines'] = df2['cuisines'].astype(str)
df2["cuisines"] = df2.loc[:, "cuisines"].apply(lambda x: x.split(",")[0])

#Convertendo valores da coluna 'average_cost_for_two' em dólares americanos(USD)
df2['average_cost_for_two'] = df2.apply(lambda x: moeda_dolar(x['average_cost_for_two'],x['currency']),axis=1)

#Substituir Outliers de da coluna average_cost_for_two baseado na mediana
lista_paises = list(df2['country_code'].unique())
for pais in lista_paises:
  df2 = mediana_pais(df2,pais) 

#Mostrar todas as colunas na visualização
pd.set_option('display.max_columns', None) 

#==========================================================
#Visão Geral
#==========================================================

#1. Quantos restaurantes únicos estão registrados?
rest_uniq = df2['restaurant_id'].nunique()

#2. Quantos países únicos estão registrados?
country_uniq = df2['country_code'].nunique()

#3. Quantas cidades únicas estão registradas?
city_uniq = df2['city'].nunique()

#4. Qual o total de avaliações feitas?
sum_votes = df2['votes'].sum()

#5. Qual o total de tipos de culinária registrados?
cuisine_uniq = df2['cuisines'].nunique()

#Mapa dos restaurantes
def criar_mapa(df2):
    map_ = folium.Map(zoom_starts=20)
    marker_cluster = MarkerCluster().add_to(map_)
    for index, row in df2.iterrows():
        folium.Marker(location=[row['latitude'], row['longitude']],
                      icon=folium.Icon(icon='cutlery', color=row['rating_color']),
                      popup=f"<b>{row['restaurant_name']}</b><br><br>"
                            f"Preço: ${round(row['average_cost_for_two'], 2)}\n"
                            f"Avaliação:{row['aggregate_rating']}/5.0\n"
                            f"Tipo:{row['cuisines']}"
                     ).add_to(marker_cluster)
    return map_    
    

#=====================================================================================
#=====================================================================================

#Streamlit

#=====================================================================================
#=====================================================================================

#==========================================================
#Streamlit Sidebar
#==========================================================
image_path = 'restaurant_logo.png'
image = Image.open(image_path)
st.sidebar.image(image,width=240)
st.sidebar.markdown("""___""")
st.sidebar.markdown("# Bem Vindo ao Food Circles")

selected_filters = st.sidebar.multiselect('# Selecione os Países que deseja filtrar abaixo:',df2['country_code'].unique(),default=['Brazil','United States of America','India','Australia','South Africa','New Zeland','England'])

selected_filters = df2['country_code'].isin(selected_filters)
location_info = df2.loc[selected_filters,:]
#==========================================================
#Página Central Streamlit
#==========================================================


st.markdown('<div style="text-align: center; font-size: 56px"><b>Food Circles Marketplace</b></div>', unsafe_allow_html=True)
with st.container():
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        col1.metric('Restaurantes Cadastrados', rest_uniq)
    with col2:
        col2.metric('Países Distintos', country_uniq)
    with col3:
        col3.metric('Cidades Distintas', city_uniq)
    with col4:
        col4.metric('Culinárias Oferecidas', cuisine_uniq)
    with col5:
        col5.metric('Avaliações na Plataforma', f"{sum_votes:,}".replace(',', '.'))   
    
st.markdown("""___""")
st.markdown('<div style="text-align: center; font-size: 36px">Encontre os melhores restaurantes da sua região aqui!</div>', unsafe_allow_html=True)
with st.container():
    map_ = criar_mapa(location_info)
    folium_static(map_, width=1024, height=600)
