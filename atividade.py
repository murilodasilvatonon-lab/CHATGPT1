import streamlit as st

st.title("Cadastro RH Já!")
st.subheader("")
nome = st.text_input("Digite seu nome: ")
email = st.text_input("Digite seu email: ")

if st.button("Cadastrar"):
    if nome and email:
        st.success(f"Funcionário {nome} cadastrado com sucesso!")
        st.balloons()
    else:
        st.error("Preencha todos os campos.")
