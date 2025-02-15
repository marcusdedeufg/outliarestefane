import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Função para detectar outliers
def detect_outliers_iqr(data, column):
    Q1 = data[column].quantile(0.25)
    Q3 = data[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    return outliers

# Interface do Streamlit
st.title('Detector de Outliers')

uploaded_file = st.file_uploader("Carregue seu arquivo Excel", type=['xlsx'])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("Visualização dos dados carregados:")
    st.write(df.head())

    column = st.selectbox('Selecione a coluna para detectar outliers', df.columns)

    if st.button('Detectar Outliers'):
        outliers = detect_outliers_iqr(df, column)
        st.write('Outliers detectados:')
        st.write(outliers)

        # Plotando o boxplot
        st.write('Boxplot:')
        fig, ax = plt.subplots()
        sns.boxplot(x=df[column], ax=ax)
        st.pyplot(fig)