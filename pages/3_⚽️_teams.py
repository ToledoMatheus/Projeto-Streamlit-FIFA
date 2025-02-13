import streamlit as st  # Para criar a interface web.



st.set_page_config(
    page_title="Teams",  # Define o título da página no navegador.
    page_icon="⚽️",  # Define o ícone da página no navegador.
    layout="wide"  # Define o layout como "wide" para utilizar mais espaço horizontal.
)


# Recupera os dados armazenados na sessão do Streamlit da 1ºpg.
df_data = st.session_state["data"]  
# Obtém a lista de clubes disponíveis no dataset.
clubes = df_data["Club"].value_counts().index  
# Cria um dropdown no sidebar para selecionar um clube.
club = st.sidebar.selectbox("CLUBE", clubes)  

# Filtra os jogadores do clube selecionado e define a coluna "Name" como índice da tabela exibida.
df_filtered = df_data[(df_data["Club"] == club)].set_index("Name")

# Exibe o logo do clube selecionado.
st.image(df_filtered.iloc[0]["Club Logo"]) 

# Exibe o nome do clube como subtítulo.
st.markdown(f"## {club}") 


# Define as colunas que serão exibidas no DataFrame (na tela).
columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']


# Escolhi o item da coluna "club" 
# e agr escolho as colunas que quero, onde seus itens estão na mesma linha desse clube:
st.dataframe(df_filtered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Habilidade", format="%d", min_value=0, max_value=100  # Configura a coluna "Overall" como uma barra de progresso.
                 ),
                 "Wage(£)": st.column_config.ProgressColumn(
                     "Salário semanal", format="£%f", min_value=0, max_value=df_filtered["Wage(£)"].max()  # Configura a coluna "Wage" como uma barra de progresso.
                 ),
                 "Photo": st.column_config.ImageColumn("Foto 3/4"),  # Configura a coluna "Photo" para exibir imagens.
                 "Flag": st.column_config.ImageColumn("Nacionalidade"),  # Configura a coluna "Flag" para exibir bandeiras dos países.
             })
# ".column_config" --> https://docs.streamlit.io/develop/api-reference/data/st.dataframe