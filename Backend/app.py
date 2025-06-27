import os
import google.generativeai as genai
from flask import Flask, request, jsonify
# from dotenv import load_dotenv

# load_dotenv()

# try:
#     genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
# except (AttributeError, KeyError):
#     print("ERRO: A chave de API do Google (GOOGLE_API_KEY) não foi encontrada. Verifique seu arquivo .env")
#     exit()

app = Flask(__name__)

PROMPT_DE_SISTEMA = """
Você é o "Agente FAQ Inteligente" do curso de Sistemas de Informação. Sua única função é responder a perguntas com base estritamente no conteúdo fornecido na "Base de Conhecimento". O conteúdo está em formato Markdown, o que ajuda a organizar a informação.

REGRAS OBRIGATÓRIAS:
1.  **NÃO ALUCINE:** Se a resposta para a pergunta não puder ser encontrada na "Base de Conhecimento", você DEVE responder exatamente com a seguinte frase: "Desculpe, não encontrei a informação na minha base de dados para responder a essa pergunta.". Não tente adivinhar, inferir ou buscar conhecimento externo.
2.  **SEJA DIRETO:** Responda apenas o que foi perguntado, de forma clara e concisa, usando as informações da base de conhecimento.
3.  **MANTENHA O FOCO:** Responda apenas sobre assuntos relacionados ao curso de Sistemas de Informação presentes no documento.

---
Base de Conhecimento (em formato Markdown):
{base_de_conhecimento}
---
"""

def carregar_base_conhecimento_md():
    try:
        with open("base_conhecimento.md", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("ERRO: Arquivo 'base_conhecimento.md' não encontrado. Verifique se ele está na mesma pasta do app.py")
        return "ERRO: Base de conhecimento não encontrada."

def gerar_resposta_ia(pergunta, chave_api_externa):
    try:
        genai.configure(api_key=chave_api_externa)
    except Exception as e:
        print(f"Erro ao configurar a API do Gemini com a chave fornecida: {e}")
        return "Chave de API inválida ou problema na configuração."

    base_de_conhecimento = carregar_base_conhecimento_md()
    if "ERRO" in base_de_conhecimento:
        return base_de_conhecimento
    
    prompt_completo = PROMPT_DE_SISTEMA.format(base_de_conhecimento=base_de_conhecimento)

    generation_config = {
        "candidate_count": 1,
        "temperature": 0.1, 
    }
    
    model = genai.GenerativeModel(
        model_name="gemini-1.5-pro-latest",
        generation_config=generation_config,
        system_instruction=prompt_completo
    )

    try:
        response = model.generate_content(pergunta)
        return response.text
    except Exception as e:
        print(f"Ocorreu um erro ao chamar a API do Gemini: {e}")
        return "Ocorreu um erro ao processar sua pergunta. Tente novamente mais tarde."

@app.route('/perguntar', methods=['POST'])
def perguntar_endpoint():
    chave_do_header = request.headers.get('x-api-key')

    if not chave_do_header:
        return jsonify({"erro": "A chave da API do Gemini é obrigatória no header 'x-api-key'."}), 401

    dados = request.get_json()

    if not dados or 'pergunta' not in dados:
        return jsonify({"erro": "A chave 'pergunta' é obrigatória no corpo da requisição."}), 400

    pergunta_usuario = dados['pergunta']
    
    resposta = gerar_resposta_ia(pergunta_usuario, chave_do_header)

    return jsonify({"resposta": resposta})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)