import streamlit as st
import time
import streamlit.components.v1 as components

# Inicialização do session_state
if 'api_key' not in st.session_state:
    st.session_state.api_key = ""
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'show_modal' not in st.session_state:
    st.session_state.show_modal = False
if 'show_key' not in st.session_state:
    st.session_state.show_key = False

# Tentar carregar a API Key do sessionStorage do navegador ao iniciar
def load_api_key_from_storage():
    components.html(
        """
        <script>
        // Tenta obter a API Key do sessionStorage
        const apiKey = sessionStorage.getItem('gemini_api_key') || '';
        // Envia para o Streamlit
        window.parent.postMessage({
            type: 'apikey',
            value: apiKey
        }, '*');
        </script>
        """,
        height=0,
    )

# Função para validar mensagem
def validar_mensagem(texto):
    palavras = texto.strip().split()
    return len(palavras) >= 5

@st.dialog("Configurar API Key")
def show_api_modal():
    with st.container():
        new_key = st.text_input("Cole sua API Key do Gemini:", type="password", key="api_key_input")
        
        # Espaçamento entre input e botões
        st.write("")  # Espaço vazio para separação
        
        # Botões com layout melhorado
        col1, col2, col3 = st.columns([2, 1, 1])  # Proporções ajustadas
        
        with col1:
            if st.button("Salvar", key="save_button", use_container_width=True):
                if new_key.strip():  # Verifica se não está vazio
                    st.session_state.api_key = new_key
                    st.session_state.show_modal = False
                    # Salvar no sessionStorage do navegador
                    components.html(
                        f"""
                        <script>
                        sessionStorage.setItem('gemini_api_key', '{new_key}');
                        </script>
                        """,
                        height=0,
                    )
                    st.rerun()
                else:
                    st.error("Por favor, insira uma API Key válida")
        
        # Espaço vazio para separação
        with col2:
            st.empty()
        
        with col3:
            if st.button("Fechar", key="close_button", use_container_width=True):
                st.session_state.show_modal = False
                st.rerun()

# Layout Principal
# Criando colunas para posicionar os botões no cabeçalho
col1, col2, col3 = st.columns([0.7, 0.2, 0.1])
with col1:
    st.title("🤖 Chatbot")
with col3:
    # Botão de configuração
    if st.button("⚙️", help="Configurar API Key", use_container_width=True):
        st.session_state.show_modal = True

# Exibir API Key se solicitado
if st.session_state.api_key and st.session_state.show_key:
    st.code(f"API Key atual: {st.session_state.api_key}")

# Carregar API Key do navegador (executa apenas uma vez)
if not st.session_state.api_key:
    load_api_key_from_storage()

# Capturar mensagem do navegador com a API Key
try:
    from streamlit.runtime.scriptrunner import RerunData, RerunException
    from streamlit.source_util import get_pages
    
    query_params = st.experimental_get_query_params()
    if 'apikey' in query_params and not st.session_state.api_key:
        st.session_state.api_key = query_params['apikey'][0]
        st.experimental_set_query_params()
        st.rerun()
except:
    pass

# Exibir modal se necessário
if st.session_state.show_modal:
    show_api_modal()

# Área de chat
chat_container = st.container()

# Exibir mensagens existentes
for message in st.session_state.messages:
    with chat_container.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do usuário
if prompt := st.chat_input("Digite sua mensagem..."):
    # Verificar API Key
    if not st.session_state.api_key:
        with chat_container.chat_message("assistant"):
            st.error("⚠️ API Key não configurada! Clique no botão ⚙️ para adicionar sua chave.")
        st.stop()
    
    # Verificar tamanho da mensagem
    if not validar_mensagem(prompt):
        with chat_container.chat_message("assistant"):
            st.error("❌ Mensagem muito curta! Digite pelo menos 5 palavras.")
        st.stop()
    
    # Adicionar mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with chat_container.chat_message("user"):
        st.markdown(prompt)
    
    # Simular resposta do assistente com animação
    with chat_container.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Simulação de resposta
        simulated_response = "Esta é uma simulação de resposta. Na implementação real, esta resposta virá da API do Google Gemini. Você digitou: " + prompt
        
        for char in simulated_response:
            full_response += char
            time.sleep(0.02)
            message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": simulated_response})