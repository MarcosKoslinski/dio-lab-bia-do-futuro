import streamlit as st
from data_loader import load_transacoes, load_perfil, load_produtos, load_historico, format_contexto
from agente import gerar_resposta

st.set_page_config(page_title="Edu - Assistente Financeiro", page_icon="💰")

st.title("💰 Edu - Seu Assistente Financeiro Inteligente")
st.markdown("Olá! Sou o Edu, aqui para ajudar com suas finanças. Pergunte sobre gastos, investimentos ou metas!")

# Carregar dados
transacoes_df, totais = load_transacoes()
perfil = load_perfil()
produtos = load_produtos()
historico_df = load_historico()
contexto = format_contexto(perfil, produtos, totais, historico_df)

# Sidebar com info do cliente
st.sidebar.header("Perfil do Cliente")
st.sidebar.write(f"**Nome:** {perfil['nome']}")
st.sidebar.write(f"**Perfil:** {perfil['perfil_investidor']}")
st.sidebar.write(f"**Renda:** R$ {perfil['renda_mensal']}")
st.sidebar.write(f"**Objetivo:** {perfil['objetivo_principal']}")

# Histórico do chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do usuário
if prompt := st.chat_input("Digite sua pergunta..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gerar resposta
    resposta = gerar_resposta(prompt, contexto)
    st.session_state.messages.append({"role": "assistant", "content": resposta})
    with st.chat_message("assistant"):
        st.markdown(resposta)