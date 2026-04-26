import requests
from config import OLLAMA_URL, MODEL

def verificar_ollama():
    """Verifica se Ollama está rodando e lista modelos."""
    try:
        url_base = OLLAMA_URL.replace('/api/generate', '')
        response = requests.get(f"{url_base}/api/tags", timeout=2)
        if response.status_code == 200:
            data = response.json()
            modelos = data.get('models', [])
            if not modelos:
                return False, "Nenhum modelo instalado. Execute: ollama pull llama2"
            modelo_names = [m.get('name', '') for m in modelos]
            return True, f"Modelos disponíveis: {', '.join(modelo_names)}"
        return False, f"Status: {response.status_code}"
    except Exception as e:
        return False, f"Erro de conexão: {str(e)}"

SYSTEM_PROMPT = """
Você é Edu, um assistente financeiro inteligente e consultivo, criado para ajudar usuários a gerenciarem suas finanças pessoais de forma segura e personalizada.

Seu objetivo principal é analisar dados financeiros do usuário, fornecer insights sobre gastos, sugerir produtos de investimento adequados ao perfil de risco, e ajudar a alcançar metas financeiras, sempre de forma educativa e preventiva.

REGRAS IMPORTANTES:
1. Baseie todas as respostas exclusivamente nos dados fornecidos no contexto (perfil, transações, produtos, histórico).
2. Nunca invente informações, taxas, rentabilidades ou conselhos financeiros não baseados nos dados.
3. Seja amigável, acessível e informal, mas inclua toques técnicos quando necessário.
4. Sempre inclua um disclaimer: "Lembre-se, isso não substitui consultoria financeira profissional."
5. Admita limitações: se não tiver dados suficientes, diga e sugira o que pode ajudar.
6. Verifique o perfil de risco antes de sugerir investimentos: para perfis conservadores, priorize produtos de baixo risco.
7. Forneça respostas concisas, mas completas, com fontes dos dados quando possível.

EXEMPLOS DE INTERAÇÃO:
- Usuário: "Quais investimentos você recomenda?"
  Agente: "Baseado no seu perfil moderado e meta de reserva de emergência, sugiro Tesouro Selic (baixo risco). Lembre-se, isso não substitui consultoria financeira profissional."
"""

def gerar_resposta(pergunta, contexto):
    ollama_ok, mensagem = verificar_ollama()
    
    if not ollama_ok:
        return f"❌ Ollama não está pronto: {mensagem}\n\nInstruções:\n1. Execute em terminal: `ollama pull phi`\n2. Execute em outro terminal: `ollama serve`\n3. Tente novamente."
    
    prompt = f"{SYSTEM_PROMPT}\n\nCONTEXTO DOS DADOS:\n{contexto}\n\nPergunta do usuário: {pergunta}\n\nResposta:"
    
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "temperature": 0.7
    }
    
    try:
        print(f"[DEBUG] Enviando para: {OLLAMA_URL}")
        print(f"[DEBUG] Modelo: {MODEL}")
        response = requests.post(OLLAMA_URL, json=payload, timeout=180)
        print(f"[DEBUG] Status: {response.status_code}")
        
        if response.status_code != 200:
            return f"❌ Erro HTTP {response.status_code}: {response.text}"
        
        result = response.json()
        return result.get("response", "Erro: Resposta vazia do modelo.")
    except requests.exceptions.Timeout:
        return "⏱️ Timeout (>180s). O modelo está muito lento. Tente com um modelo mais rápido:\n- Execute: `ollama pull phi`\n- Atualize config.py: MODEL = 'phi'\n- Recarregue o app."
    except Exception as e:
        return f"⚠️ Erro: {str(e)}. Verifique se Ollama está rodando em {OLLAMA_URL}."