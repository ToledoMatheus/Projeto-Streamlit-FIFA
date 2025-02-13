import streamlit as st  # Streamlit para criar a interface web.
import webbrowser  # webbrowser para abrir links externos no navegador.
import pandas as pd  # Pandas para manipulação de dados, fazer tabelas.
from datetime import datetime  # Importa a classe datetime para trabalhar com datas.

# Tem que nomear o código com "nº_", o número mosta a ordem das páginas

st.set_page_config(
    page_title="Home",  # Define o título da página no navegador.
    page_icon="🏠",  # Define o ícone da página no navegador.
    layout="wide"  # Define o layout como "wide" para utilizar mais espaço horizontal.
)



# Verifica se os dados já foram carregados na sessão do Streamlit.
if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)  # Lê o arquivo CSV na pasta datasets e define a coluna 0 como índice.
    
    # Filtros:
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]  # Filtra jogadores que a coluna "Contract Valid Until" seja  >= ano atual.
    df_data = df_data[df_data["Value(£)"] > 0]  # Filtra jogadores com a coluna "Value(£)" maior que zero.

    # Estabelecendo uma ordem:
    df_data = df_data.sort_values(by="Overall", ascending=False)  # Ordena os jogadores por ordem decrescente pela coluna "Overall".
 
    # Armazena os dados filtrados na sessão do Streamlit para uso posterior:
    st.session_state["data"] = df_data  # isso vai ser colocado nas outras páginas 




st.markdown("# FIFA23 OFFICIAL DATASET! ⚽️")  # Título principal da página.
st.sidebar.markdown("Desenvolvido por [Asimov Academy](https://asimov.academy)")  # Informação no sidebar (canto esquerdo)


# Botão que redireciona o usuário para o site do Kaggle onde os dados estão hospedados.
btn = st.button("Acesse os dados no Kaggle")
if btn: # Se ele transicionar para o status True
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")


# Descrição detalhada do conjunto de dados.
st.markdown(
    """
    O conjunto de dados
    de jogadores de futebol de 2017 a 2023 fornece informações 
    abrangentes sobre jogadores de futebol profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos 
    do jogador, características físicas, estatísticas de jogo, detalhes do contrato e 
    afiliações de clubes. 
    
    Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para 
    analistas de futebol, pesquisadores e entusiastas interessados em explorar vários 
    aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de 
    desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e 
    desenvolvimento do jogador ao longo do tempo.
"""
)


st.write("Arquivo 'CLEAN_FIFA23_official_data.csv' sem filtro:")
df = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv")
df
