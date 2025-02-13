import streamlit as st  # Para criar a interface web.



st.set_page_config(
    page_title="Players",  # Define o título da página.
    page_icon="💩",  # Define o ícone da página.
    layout="wide"  # Define o layout como "wide" para utilizar mais espaço horizontal.
)

# Recupera os dados armazenados na sessão do Streamlit da 1ºpg
df_data = st.session_state["data"] # --> é o arquivo em .csv com o filtro e ordenação feito na 1ºpg

# Obtém a lista ".value_counts().index" da coluna "Club" disponíveis no dataset.
clubes = df_data["Club"].value_counts().index
# Cria um dropdown("caixa de seleção") no sidebar(lado esquerdo) para selecionar um clube.
clube = st.sidebar.selectbox("Clube", clubes)  


# Filtra os jogadores da coluna club selecionado.
df_players = df_data[(df_data["Club"] == clube)]
# Agora que filtrou o item da coluna "club" --> 
# --> Filtrar todos da coluna "Name" que estão na linha desse clube e faz uma lista ".value_counts().index "
players = df_players["Name"].value_counts().index  
# Cria um dropdown("caixa de seleção") no sidebar(lado esquerdo)
player = st.sidebar.selectbox("Jogador", players) 


# Obtém as informações do jogador selecionado:
# ".iloc[0]" --> Para acessar linhas ou colunas de um DataFrame do Pandas por posição,
# seleciona a 1º linha desse DataFrame filtrado.Isso garante que estamos trabalhando com os dados de um único jogador, mesmo que haja múltiplas entradas com o mesmo nome.
player_stats = df_data[df_data["Name"] == player].iloc[0]
# Exibe o item da coluna "Photo" desse jogador
st.image(player_stats["Photo"]) 
# Exibe o item da coluna "Name" desse jogador como título 
st.title(player_stats["Name"])  
# Exibe  o item da coluna "Club" desse jogador
st.markdown(f"**Clube:** {player_stats['Club']}")
# Exibe o item da coluna "Position" desse jogador
st.markdown(f"**Posição:** {player_stats['Position']}")  


# Divide a tela em 4 colunas para exibir informações uma do lado da outra.
col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")  # Exibe o item da coluna "Age" desse jogador
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}")  # Converte altura de cm para metros e exibe.
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453:.2f}")  # Converte peso de libras para kg e exibe.

# Adiciona uma linha divisória na tela.
st.divider()  
# Exibe o item da coluna "Overall"
st.subheader(f"Nivel de habilidade: {player_stats['Overall']}") 
# Exibe uma barra de progresso com o valor de "Overall".
st.progress(int(player_stats["Overall"]))  


# Divide a tela em 4 colunas para exibir métricas.
# https://docs.streamlit.io/develop/api-reference/data/st.metric
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")  # Exibe o valor de mercado formatado.
col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")  # Exibe a remuneração semanal formatada.
col3.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")  # Exibe a cláusula de rescisão formatada.

# :, -> Adiciona vírgulas a números grandes.
# Ex.: 1000000 --> 1,000,000


# https://docs.streamlit.io/develop/api-reference/text 
#.markdown", ".subheader" e ".title" são tamanhos de escrita.
