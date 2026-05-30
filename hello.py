import streamlit as st

st.title("Bem-vindo à minha primeira página web.")
st.subheader("Desenvolvido por: Murilo")

nome = st.text_input("Digite seu nome: ")
idade = st.text_input("Digite seu idade: ")

if st.button("Cadastrar"):
    if nome and idade:
        st.success(f"Funcionário {nome} cadastrado com sucesso!")
        st.balloons()
    else:
        st.error("Preencha todos os campos.")
        

