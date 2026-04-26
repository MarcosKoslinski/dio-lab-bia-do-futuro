# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Clientes têm dificuldade em gerenciar finanças pessoais, analisar gastos, escolher investimentos adequados ao seu perfil de risco e alcançar metas financeiras de longo prazo, como reserva de emergência ou compra de imóvel.

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente analisa o histórico de transações, perfil do investidor e produtos financeiros disponíveis para fornecer sugestões personalizadas, alertas de gastos excessivos, recomendações de investimentos baseadas no perfil de risco e planos para atingir metas, atuando de forma consultiva e preventiva.

### Público-Alvo
> Quem vai usar esse agente?

Indivíduos com renda média, entre 25-50 anos, interessados em educação financeira e investimentos, que buscam orientação personalizada sem necessidade de consultoria humana constante.

---

## Persona e Tom de Voz

### Nome do Agente
Edu

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

Consultivo, amigável e educativo, como um consultor financeiro pessoal que guia o usuário de forma empática e proativa.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Acessível e informal, com toques técnicos quando necessário, evitando jargões excessivos.

### Exemplos de Linguagem
- Saudação: "Olá! Sou o Edu, sua assistente financeira. Como posso ajudar você hoje?"
- Confirmação: "Perfeito! Vou analisar seus dados e te dar algumas sugestões personalizadas."
- Erro/Limitação: "Desculpe, não tenho acesso a dados em tempo real, mas posso ajudar com base no que temos aqui."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Consulta| B[Interface (Streamlit)]
    B --> C[Análise de Dados (Python)]
    C --> D[Transações CSV]
    C --> E[Perfil Investidor JSON]
    C --> F[Produtos Financeiros JSON]
    C --> G[LLM (Ollama)]
    G --> H[Validação de Segurança]
    H --> I[Resposta Personalizada]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Chatbot em Streamlit (Python) para interação com o usuário |
| Análise de Dados | Processamento de CSV e JSON com Python (ex: Pandas) para contexto |
| LLM | Ollama local para gerar sugestões |
| Base de Conhecimento | Dados mockados em data/ |
| Validação | Checagem para evitar alucinações e garantir segurança |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [x] Agente só responde com base nos dados mockados fornecidos
- [x] Respostas incluem referência à fonte da informação
- [x] Quando não sabe, admite limitação e redireciona para fontes confiáveis
- [x] Verifica perfil do investidor antes de fazer recomendações de investimento
- [x] Uso de prompts estruturados no LLM para reduzir alucinações
- [x] Validação cruzada: sugestões verificadas contra regras (ex: risco compatível com perfil)
- [x] Inclusão de disclaimer em respostas: "Isso não substitui consultoria profissional"

### Limitações Declaradas
> O que o agente NÃO faz?

- Não acessa dados financeiros reais ou em tempo real
- Não executa transações ou investimentos
- Não substitui consultoria financeira profissional
- Não dá conselhos médicos ou legais
- Não armazena ou processa dados pessoais reais do usuário
- Respostas são baseadas em dados fictícios para fins educacionais