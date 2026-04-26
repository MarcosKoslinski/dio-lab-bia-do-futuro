# Código da Aplicação Edu

Esta pasta contém o código do Edu, agente financeiro inteligente.

## Estrutura

```
src/
├── app.py              # Aplicação principal (Streamlit)
├── agente.py           # Lógica do agente e integração com Ollama
├── data_loader.py      # Carregamento e processamento de dados
├── config.py           # Configurações (URLs, etc.)
└── requirements.txt    # Dependências
```

## Como Executar o Edu

### Pré-requisitos
- Python 3.8+
- Ollama instalado (https://ollama.ai/)

### Passos
1. **Instale as dependências:**
   ```
   pip install -r requirements.txt
   ```

2. **Instale e execute o Ollama:**
   - Baixe e instale Ollama.
   - Execute um modelo: `ollama run llama2` (ou outro modelo em português, como `llama2:7b`).
   - Verifique se está rodando em http://localhost:11434.

3. **Execute a aplicação:**
   ```
   streamlit run app.py
   ```

4. **Acesse:** Abra o navegador em http://localhost:8501.

### Teste
- Pergunte: "Como estão meus gastos este mês?"
- Esperado: Análise baseada em dados, com disclaimer.

### Notas
- Dados carregados de ../data/.
- Ajuste config.py se necessário (modelo Ollama, caminhos).
```

## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
streamlit run app.py
```
