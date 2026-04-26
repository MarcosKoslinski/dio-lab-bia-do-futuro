# 🤖 Agente Financeiro Inteligente com IA Generativa

## Contexto

Os assistentes virtuais no setor financeiro estão evoluindo de simples chatbots reativos para **agentes inteligentes e proativos**. Neste desafio, você vai idealizar e prototipar um agente financeiro que utiliza IA Generativa para:

- **Antecipar necessidades** ao invés de apenas responder perguntas
- **Personalizar** sugestões com base no contexto de cada cliente
- **Cocriar soluções** financeiras de forma consultiva
- **Garantir segurança** e confiabilidade nas respostas (anti-alucinação)

> [!TIP]
> Na pasta [`examples/`](./examples/) você encontra referências de implementação para cada etapa deste desafio.

---

## O Que Você Deve Entregar

### 1. Documentação do Agente

Defina **o que** seu agente faz e **como** ele funciona:

- **Caso de Uso:** Resolve dificuldades em gerenciar finanças pessoais, analisar gastos, escolher investimentos adequados ao perfil de risco e alcançar metas de longo prazo como reserva de emergência.
- **Persona e Tom de Voz:** Agente chamado Edu, consultivo e amigável, acessível e informal, com toques técnicos quando necessário.
- **Arquitetura:** Interface em Streamlit (Python), análise de dados com Pandas, LLM via Ollama local, validação para evitar alucinações.
- **Segurança:** Respostas baseadas em dados mockados, uso de prompts estruturados, validação cruzada, inclusão de disclaimers e limitações declaradas.

📄 **Template:** [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

### 2. Base de Conhecimento

Utilize os **dados mockados** disponíveis na pasta [`data/`](./data/) para alimentar seu agente:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `transacoes.csv` | CSV | Analisar padrões de gastos e fornecer alertas ou insights |
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores e histórico de atendimentos |
| `perfil_investidor.json` | JSON | Personalizar recomendações baseadas no perfil de risco e metas |
| `produtos_financeiros.json` | JSON | Sugerir produtos financeiros adequados ao perfil e objetivos |

Os dados são carregados em Python (Pandas para CSV, json para JSON) com pré-processamento para agregações (ex: totais por categoria), e integrados dinamicamente nos prompts do LLM via Ollama para personalização e insights.

📄 **Template:** [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### 3. Prompts do Agente

Documente os prompts que definem o comportamento do Edu:

- **System Prompt:** Instruções gerais de comportamento, regras de segurança e persona consultiva
- **Exemplos de Interação:** Cenários de análise de gastos, sugestões de investimentos e acompanhamento de metas
- **Tratamento de Edge Cases:** Admissão de limitações, redirecionamento e solicitações de contexto adicional
- **Observações e Aprendizados:** Ajustes para reduzir alucinações e melhorar segurança

📄 **Template:** [`docs/03-prompts.md`](./docs/03-prompts.md)

---

### 4. Aplicação Funcional

Desenvolva o protótipo do Edu:

- **Interface:** Chatbot em Streamlit para interações amigáveis.
- **LLM:** Integração com Ollama local para respostas seguras e rápidas.
- **Base de Conhecimento:** Carregamento de dados CSV/JSON para personalização.
- **Funcionalidades:** Análise de gastos, sugestões de investimentos, acompanhamento de metas.

📁 **Pasta:** [`src/`](./src/)

---

### 5. Avaliação e Métricas

Descreva como você avalia a qualidade do Edu:

- **Métricas de Qualidade:** Assertividade, segurança, coerência, relevância
- **Métricas de Usuário:** Satisfação, engajamento, retenção
- **Métricas Técnicas:** Latência, throughput, custo, taxa de erro, uptime
- **Métricas Avançadas:** Taxa de alucinação, precisão, relevância (BLEU), NPS, retenção
- **Cenários de Teste:** 5 testes estruturados com perguntas e respostas esperadas

📄 **Template:** [`docs/04-metricas.md`](./docs/04-metricas.md)
- Coerência com o perfil do cliente

📄 **Template:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch

Apresente o Edu em um pitch de 3 minutos:

- **Problema:** Dificuldade em gerenciar finanças pessoais e tomar decisões seguras.
- **Solução:** Assistente IA consultivo com análise de dados e sugestões personalizadas.
- **Demonstração:** Interface Streamlit mostrando interações reais.
- **Diferencial e Impacto:** IA local segura, promovendo educação financeira e decisões melhores.

📄 **Template:** [`docs/05-pitch.md`](./docs/05-pitch.md)

---

## Conclusão

O projeto Edu está totalmente documentado: arquitetura definida, prompts criados, métricas estabelecidas e pitch preparado. Próximo passo: implementar o protótipo funcional em `src/` para demonstração prática.

---

## Ferramentas Sugeridas

Todas as ferramentas abaixo possuem versões gratuitas:

| Categoria | Ferramentas |
|-----------|-------------|
| **LLMs** | [ChatGPT](https://chat.openai.com/), [Copilot](https://copilot.microsoft.com/), [Gemini](https://gemini.google.com/), [Claude](https://claude.ai/), [Ollama](https://ollama.ai/) |
| **Desenvolvimento** | [Streamlit](https://streamlit.io/), [Gradio](https://www.gradio.app/), [Google Colab](https://colab.research.google.com/) |
| **Orquestração** | [LangChain](https://www.langchain.com/), [LangFlow](https://www.langflow.org/), [CrewAI](https://www.crewai.com/) |
| **Diagramas** | [Mermaid](https://mermaid.js.org/), [Draw.io](https://app.diagrams.net/), [Excalidraw](https://excalidraw.com/) |

---

## Estrutura do Repositório

```
📁 lab-agente-financeiro/
│
├── 📄 README.md
│
├── 📁 data/                          # Dados mockados para o agente
│   ├── historico_atendimento.csv     # Histórico de atendimentos (CSV)
│   ├── perfil_investidor.json        # Perfil do cliente (JSON)
│   ├── produtos_financeiros.json     # Produtos disponíveis (JSON)
│   └── transacoes.csv                # Histórico de transações (CSV)
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md     # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # Engenharia de prompts
│   ├── 04-metricas.md                # Avaliação e métricas
│   └── 05-pitch.md                   # Roteiro do pitch
│
├── 📁 src/                           # Código da aplicação
│   └── app.py                        # (exemplo de estrutura)
│
├── 📁 assets/                        # Imagens e diagramas
│   └── ...
│
└── 📁 examples/                      # Referências e exemplos
    └── README.md
```

---

## Dicas Finais

1. **Comece pelo prompt:** Um bom system prompt é a base de um agente eficaz
2. **Use os dados mockados:** Eles garantem consistência e evitam problemas com dados sensíveis
3. **Foque na segurança:** No setor financeiro, evitar alucinações é crítico
4. **Teste cenários reais:** Simule perguntas que um cliente faria de verdade
5. **Seja direto no pitch:** 3 minutos passam rápido, vá ao ponto
