import streamlit as st

st.title("Secretaria SENAI Americana")
st.subheader("Conheça os nossos cursos")

st.write("I.A. Generativa, Power BI, Empilhadeira, Excel, Eletricista Instalador")
st.markdown("**Atenção** : Verifique se existem vagas disponíveis.")

nome = st.text_input("Digite o seu nome: ")
idade = st.number_input("Digite a sua idade: ", min_value=16, max_value=99)
cursoEscolhido = st.selectbox("Cursos disponíveis",["I.A.", "Generativa", "Excel", "Power BI", "Empilhadeira", "Excel", "Eletricista Instalador"])
Termos = st.checkbox("Ao clicar aqui, você aceia os termos e condições")

if st.button ("Enviar resposta"):
    if nome and idade and cursoEscolhido and Termos:
        st.success()
    else:
        st.error("")