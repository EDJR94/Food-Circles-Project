# 1. Problema de Negócio

A empresa Food Circles é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Food Circles, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.

O CEO precisa tomar as melhores decisões estratégicas , e para isso, ele precisa que seja feita uma análise nos dados da empresa e que sejam gerados dashboards em uma única ferramenta para que o ele possa consultar rapidamente e tomar decisões rápidas. O CEO gostaria de ver as seguintes visões de crescimento:

## Visão Geral:
1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?

## Visão País:
1. Qual o nome do país que possui mais cidades registradas?
2. Qual o nome do país que possui mais restaurantes registrados?
3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4
registrados?
4. Qual o nome do país que possui a maior quantidade de tipos de culinária
distintos?
5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem
entrega?
7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam
reservas?
8. Qual o nome do país que possui, na média, a maior quantidade de avaliações
registrada?
9. Qual o nome do país que possui, na média, a maior nota média registrada?
10. Qual o nome do país que possui, na média, a menor nota média registrada?
11. Qual a média de preço de um prato para dois por país?

## Visão Cidade:
1. Qual o nome da cidade que possui mais restaurantes registrados?
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de
4?
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de
2.5?
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária
distintas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
reservas?
7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem
entregas?
8. Qual o nome da cidade que possui a maior quantidade de restaurantes que
aceitam pedidos online?

## Visão Restaurantes:
1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
2. Qual o nome do restaurante com a maior nota média?
3. Qual o nome do restaurante que possui o maior valor de uma prato para duas
pessoas?
4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor
média de avaliação?
5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que
possui a maior média de avaliação?
6. Os restaurantes que aceitam pedido online são também, na média, os
restaurantes que mais possuem avaliações registradas?
7. Os restaurantes que fazem reservas são também, na média, os restaurantes que
possuem o maior valor médio de um prato para duas pessoas?
8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América
possuem um valor médio de prato para duas pessoas maior que as churrascarias
americanas (BBQ)?

## Visão Culinária:
1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do
restaurante com a maior média de avaliação?
2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do
restaurante com a menor média de avaliação?
3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do
restaurante com a maior média de avaliação?
4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do
restaurante com a menor média de avaliação?
5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do
restaurante com a maior média de avaliação?
6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do
restaurante com a menor média de avaliação?
7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do
restaurante com a maior média de avaliação?
8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do
restaurante com a menor média de avaliação?
9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do
restaurante com a maior média de avaliação?
10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do
restaurante com a menor média de avaliação?
11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas
pessoas?
12. Qual o tipo de culinária que possui a maior nota média?
13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos
online e fazem entregas?

# 2. Premissas
1. Marketplace foi o modelu assumido para o negócio
2. Dentre as visões, as assumidas para o negócio foram: Visão Geral, Visão País, Visão Culinária e Visão Cidade.

# 3. Estratégia de Solução

1. O dashboard foi construído com base nas métricas das principais visões do modelo de negócio da empresa:
    1. Visão Geral
    2. Visão País
    3. Visão Cidades
    4. Visão Culinária
2. Para cada visão é representado pelo seguintes conjuntos de métricas:
    
    ### Visão Geral:
    
    1. Restaurantes cadastrados
    2. Países distintos cadastrados
    3. Cidades distintas cadastradas.
    4. Culinárias oferecidas.
    5. Avaliações totais feitas na plafatorma.
    6. Mapa com a posição dos restaurantes
    
    ### Visão País:
    
    1. Quantidade de restaurantes por País
    2. Preço de Um Prato Para 2 por País
    3. Tipos de culinária por País
    4. Média de avaliação por País
    
    ### Visão Culinária:
    
    1. Restaurante maior quantidade de avaliações
    2. Restaurante melhor avaliado
    3. Restaurante com a maior preço Para 2
    4. Culinária melhor avaliada
    
    ### Visão Cidades:
    
    1. Quantidade de restaurante por Cidade
    2. Cidade com melhores e piores avaliações
    3. Cidades com maiores preços Para 2
    4. Cidades que mais aceitam entregas online.

# 4. Top Insights de dados

1. Os restaurantes que aceitam pedidos online não necessariamente são os que mais possuem avaliações na plataforma. 
2. Os restaurantes que fazem reservas são, na média, os que possuem o maior valor médio de Um Prato Para 2 Pessoas.
3. Por mais que os EUA tenham a maior quantidade de restaurates com o maior nível de preço entre todos os países, ele não possui, na média, os restaurante com maior preço de Um Prato Para 2 Pessoas.

# 5. Produto Final

Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet.

O painel pode ser acessado através desse link: [https://projects-foodcircle.streamlit.app/](https://projects-foodcircle.streamlit.app/)

# 6. Conclusão

O objetivo desse projeto é criar um dashboard com gráficos/tabelas que exibam as métricas de negócio da melhor forma possível para o CEO tomar suas decisões.

Podemos concluir que o dashboard cumpre o que foi pedido pelo CEO, já que ele pode selecionar métricas desejadas por ele da forma que melhor preferir, englobando as principais visões marketplace Food Circles.

# 7. Próximos Passos

1. Podemos observar, portanto, que a maior parte do negócio está concentrado nos EUA e na Índia, onde se encontram restaurantes consolidados com bastante avaliações. O CEO deve se concentrar, agora, em países que a plataforma vem alcançando pouco e com avaliações baixas, como no Brazil, por exemplo.
2. Reduzir a quantidade de métricas em cada visão para focar em mais em fazer as perguntas certas.
