<h1>Dashboard Índice de Percepção de Corrupção Mundial</h1>

<h2>Visualização temporária</h2>
<p>(Recarregue a página caso o GIF não apareça)</p>

<img src="gif.gif" alt=gif>

<h2>O projeto</h2>
<p> Em resumo, o projeto é um aplicativo web interativo, desenvolvido com o objetivo de obter uma forma melhor de visualizar os dados do índice de corrupção mundial.</p>

<h3>Arquivos necessários para rodar o aplicativo</h3>
<p>É preciso ter o Python instalado no computador e as bibliotecas necessárias.</p>
<ul>
    <li>app.py</li>
    <li>new_corruption_data.csv</li>
    <li>countries.geo.json</li>
</ul>

<h2>Arquivos utilizados para manipulação dos dados</h2>
<ul>
    <li>transformacao.py</li>
    <li>corruption_data.csv</li>
    <li>regional_codes_iso3166.csv</li>
    <li>ajuste_df.csv</li>
</ul>

<h2>Tecnologias utilizadas</h2>
<ul>
    <li>Python v3.10.7</li>
    <li>Pandas v1.5.0</li>
    <li>Plotly v5.10.0</li>
    <li>Dash v2.6.2</li>
    <li>Dash Core Components v2.0.0</li>
    <li>Dash HTML Components v2.0.0</li>
    <li>Dash Bootstrap Components v1.2.1</li>
    <li>Json</li>
    <li>CSV</li>
</ul>

<h2>Desenvolvimento</h2>

<h3>Transformação da estrutura dos dados</h3>
<p>Os dados iniciais contidos no arquivo <u>corruption_data.csv</u> possuem uma estrutura de dados larga, com os índices como valores das colunas de anos, possível de se trabalhar, porém, resolvi alterar por conveniência. O meu objetivo era ter os dados dos anos em uma única coluna, o mesmo para os índices.</p>
<p>Para obter o resultado que eu esperava, criei o arquivo <u>transformacao.py</u> para efetuar a manipulação em separado, utilizei a biblioteca Pandas do  Python para lidar com isso. No decorrer do processo, também precisei mesclar dados de identificadores exclusivos de países, para isso, utilizei uma tabela chamada <u>regional_codes_iso3166.csv</u> da Organização Internacional de Normalização (ISO). Por fim, por conta de alguns nomes de países não coincidirem entre as tabelas, precisei fazer um mapeamento manual de 23 países, o arquivo <u>ajuste_df.csv</u>. O arquivo final chama-se <u>new_corruption_data.csv</u></p>

<h3>Visualização dos dados</h3>
<p>Para obter a visualização dos dados já transformados, fiz grande uso das bibliotecas <b>Plotly Express</b> para criação dos gráficos, <b>Dash</b> para criação do aplicativo, <b>Dash Core Components</b> para utilização dos componentes gráficos, <b>Dash HTML Components</b> para escrever em HTML com sintaxe Python e o <b>Dash Bootstrap Components</b> para estilização e estruturação (que abstrai o uso de CSS).</p>

<h2>Objetivo</h2>
<p>O projeto foi desenvolvido com o mero objetivo de obtenção de prática com as ferramentas e de desenvolvimento do conhecimento.</p>



