import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('df.csv')
df = df.drop(columns=['Unnamed: 0'])
st.title('Наш датафрейм:')
st.dataframe(df)


try:
    column = st.selectbox(
        "Выбери столбец", tuple(df.columns[1:])
    )
    if not column:
        st.error("Ошибка")

    fig, ax = plt.subplots()

    ax.hist(df[column])
    plt.grid()
    st.title(f"График распределения {column}:")
    st.pyplot(fig)
except:
    st.text("Ошибка, выбери другой признак")


st.title('Матрица корреляций:')
corr = df.corr()
fig, ax = plt.subplots(figsize=(18,18))
sns.heatmap(corr, cmap="Blues", annot=True)
st.write(fig)


try:
    column = st.selectbox(
        "Выбери с признак для сравнения с целевой переменной", tuple(df.columns[1:])
    )
    if not column:
        st.error("Ошибка, попробуй выбрать другой признак")

    fig, ax = plt.subplots(figsize=(18,10))
    sns.barplot(x=column, y='TARGET', data=df)
    st.title(f"График зависимости {column} от целевой переменной:")
    st.pyplot(fig)
except:
    st.text("Ошибка, выбери другой признак")

st.title('Основные статистики по нашему датафрейму:')
st.dataframe(df.describe())
