import streamlit as st

st.title("Freddy Fazbear's Pizza")
st.image("pizza.jpg", width=550, use_container_width=True)

nome = st.text_input("Digite seu nome: ")
cidade = st.text_input("Digite sua cidade: ")
bairro = st.text_input("Digite seu bairro: ")

pizza = st.selectbox(
    "Escolha sua pizza favorita",
    ["Calabresa", "Frango", "Quatro Queijos"]
)

if st.button("Envia r Pesquisa"):
    if nome and cidade and bairro:
        st.success(
            f"Obrigado, {nome}! Você é de {bairro}, {cidade} e escolheu a pizza {pizza}."
        )
    else:
        st.error("Preencha todos os campos.")