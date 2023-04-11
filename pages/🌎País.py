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

st.set_page_config(page_title='País', page_icon='🌎', layout='wide')

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
#Visão Países
#==========================================================

#1. Qual o nome do país que possui mais restaurantes registrados?
cols = ['restaurant_id','country_code']
df2_aux = df2.loc[:,cols].groupby('country_code').nunique().reset_index()
df2_aux = df2_aux.sort_values(by='restaurant_id',ascending=False)
px.bar(df2_aux,x='country_code',y='restaurant_id',labels={'country_code: País', 'restaurant_id: Restaurantes'})

#2. Qual a média de preço de um prato para dois por país?
cols = ['average_cost_for_two','country_code',]
df2_aux = df2.loc[:,cols].groupby(['country_code']).mean().reset_index().sort_values(by='average_cost_for_two',ascending=False)
px.bar(df2_aux,x='country_code',y='average_cost_for_two',labels={'country_code: País', 'average_cost_for_two: Preço Médio'})

#3. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
cols = ['country_code','cuisines']
df2_aux = df2.loc[:,cols].groupby('country_code').nunique().reset_index()
df2_aux = df2_aux.sort_values(by='cuisines', ascending=False)
px.bar(df2_aux,x='country_code',y='cuisines',labels={'country_code: País', 'cuisines: Culinárias'})

#4. Qual o nome do país que possui, na média, a maior nota média registrada?
cols = ['aggregate_rating', 'country_code']
df2_aux = df2.loc[:,cols].groupby('country_code').agg({'aggregate_rating': ['mean','std','count']})
df2_aux.columns = ['media_rating','std_rating','count_rating']
df2_aux = df2_aux.sort_values(by='media_rating',ascending=False)
df2_aux = df2_aux.reset_index()
px.bar(df2_aux,x='country_code',y='media_rating',error_y='std_rating',labels={'country_code: País', 'media_rating: Nota Média'})
   
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

selected_filters_country = st.sidebar.multiselect('Selecione os Países que deseja filtrar abaixo:',df2['country_code'].unique(),default=['Brazil','United States of America','Australia','South Africa','New Zeland','England'])
price_slider = st.sidebar.slider('Selecione até qual valor($) de Um Prato para Dois',
                             value=755,
                             min_value=0,
                             max_value=755)

selected_filters_country = df2['country_code'].isin(selected_filters_country) 
df2 = df2.loc[selected_filters_country,:]
filtro_slider = df2['average_cost_for_two'] <= price_slider
df2 = df2.loc[filtro_slider,:]
#==========================================================
#Página Central Streamlit
#==========================================================


st.markdown('<div style="text-align: center; font-size: 56px"><b>Visão Países</b></div>', unsafe_allow_html=True)
st.markdown("""___""")
with st.container():
    st.markdown('<div style="text-align: center; font-size: 24px"><b>Quantidade de Restaurantes por País</b></div>', unsafe_allow_html=True)
    cols = ['restaurant_id','country_code']
    df2_aux = df2.loc[:,cols].groupby('country_code').nunique().reset_index()
    df2_aux = df2_aux.sort_values(by='restaurant_id',ascending=False)
    fig = px.bar(df2_aux,x='country_code',y='restaurant_id',labels={'country_code': 'País', 'restaurant_id': 'Restaurantes'})
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""___""")

with st.container():
    st.markdown('<div style="text-align: center; font-size: 24px"><b>Preço de Um Prato Para 2 por País</b></div>', unsafe_allow_html=True)
    cols = ['average_cost_for_two','country_code',]
    df2_aux = df2.loc[:,cols].groupby(['country_code']).mean().reset_index().sort_values(by='average_cost_for_two',ascending=False)
    fig = px.bar(df2_aux,x='country_code',y='average_cost_for_two',labels={'country_code': 'País', 'average_cost_for_two': 'Preço Médio(USD $)'})
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""___""")

with st.container():
    col1,col2 = st.columns(2)
    with col1:
        st.markdown('<div style="text-align: center; font-size: 24px"><b>Tipos de Culinária por País</b></div>', unsafe_allow_html=True)
        cols = ['country_code','cuisines']
        df2_aux = df2.loc[:,cols].groupby('country_code').nunique().reset_index()
        df2_aux = df2_aux.sort_values(by='cuisines', ascending=False)
        fig = px.bar(df2_aux,x='country_code',y='cuisines',labels={'country_code': 'País', 'cuisines': 'Culinárias'})
        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.markdown('<div style="text-align: center; font-size: 24px"><b>Média de avaliação por País</b></div>', unsafe_allow_html=True)
        cols = ['aggregate_rating', 'country_code']
        df2_aux = df2.loc[:,cols].groupby('country_code').agg({'aggregate_rating': ['mean','std','count']})
        df2_aux.columns = ['media_rating','std_rating','count_rating']
        df2_aux = df2_aux.sort_values(by='media_rating',ascending=False)
        df2_aux = df2_aux.reset_index()
        fig = px.bar(df2_aux, x='country_code', y='media_rating', error_y='std_rating', labels={'country_code': 'País', 'media_rating': 'Nota Média'})
        fig.update_traces(error_y_color='darkred')
        st.plotly_chart(fig, use_container_width=True)
        
            
    
    

