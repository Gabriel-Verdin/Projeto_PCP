import streamlit as st

st.title("Cadastro de Produtos")

hc = st.text_input("Digite o HC do Produto: ")
descricao = st.text_input("Digite a Descrição do Produto: ")
media_vendas = st.number_input("Digite a Média de Vendas: (0 se não possuir)", min_value=0, max_value=100000)
partida = st.number_input("Digite a Partida de Produção: (0 se não possuir)", min_value=0, max_value=100000)

if st.button("Cadastrar Produto"):

    st.text("Resumo do Cadastro:")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("**HC**")
        st.text(hc)

    with col2:
        st.markdown("**Descrição**")
        st.text(descricao)

    with col3:
        st.markdown("**Média de Vendas**")
        st.text(media_vendas)

    with col4:
        st.markdown("**Partida**")
        st.text(partida)

#if st.button("Salvar Cadastro"):
    #if hc is None or descricao is None :
        #st.write("Insira um Cadastro Válido!")
    #else:
        #st.write("Produto salvo com sucesso!")