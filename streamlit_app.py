import streamlit as st
import pandas as pd
import plotly.express as px

# Título da aplicação
st.title('Análise de Sentimento dos Simpsons')

# Função para carregar e processar os dados
@st.cache_data  # Cache para melhorar o desempenho
def load_and_process_data():
    try:
        df = pd.read_csv('frases_classificadas.csv')
        sentimento_counts = df['classificacao'].value_counts().to_dict()
        return sentimento_counts
    except FileNotFoundError:
        st.error("O arquivo 'frases_classificadas.csv' não foi encontrado.")
        return None


sentimento_counts = load_and_process_data()


if sentimento_counts:
    # Criar o gráfico de pizza
    fig = px.pie(
        names=list(sentimento_counts.keys()),
        values=list(sentimento_counts.values()),
        title='Distribuição de Sentimentos',
        color_discrete_sequence=px.colors.sequential.RdBu
    )

    # Mostrar o gráfico no Streamlit
    st.plotly_chart(fig)

    # Mostrar a tabela com os dados (opcional)
    st.write("Tabela de contagem de sentimentos:")
    st.dataframe(pd.DataFrame({'Sentimento': list(sentimento_counts.keys()), 'Contagem': list(sentimento_counts.values())}))