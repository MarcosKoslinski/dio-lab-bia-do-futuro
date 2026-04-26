# Avaliação e Métricas

## Como Avaliar o Edu

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Defina perguntas e respostas esperadas baseadas nos dados mockados;
2. **Feedback real:** Pessoas testam o agente e avaliam com notas de 1 a 5.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu corretamente com base nos dados? | Perguntar total de gastos e receber valor exato do CSV |
| **Segurança** | O agente evitou alucinações e incluiu disclaimers? | Perguntar investimento e verificar se perfil foi considerado |
| **Coerência** | A resposta faz sentido para o perfil e contexto do cliente? | Sugerir produtos de baixo risco para perfil moderado |
| **Relevância** | A resposta é útil e focada no problema do usuário? | Fornecer insights acionáveis sobre metas |

---

## Métricas de Usuário

| Métrica | O que avalia | Como medir |
|---------|--------------|------------|
| **Satisfação** | O usuário ficou satisfeito com a resposta? | Pesquisa pós-interação (1-5 estrelas) |
| **Engajamento** | O usuário interagiu mais ou pediu esclarecimentos? | Número de mensagens por sessão |
| **Retenção** | O usuário voltou a usar o agente? | Taxa de retorno em sessões subsequentes |

---

## Métricas Técnicas

| Métrica | O que avalia | Como medir |
|---------|--------------|------------|
| **Latência** | Tempo de resposta do agente | Média de segundos por resposta (meta: <3s) |
| **Throughput** | Capacidade de processar múltiplas consultas | Consultas por minuto |
| **Custo** | Recursos utilizados (API, energia) | Custo por interação (para Ollama local: baixo) |

---

## Exemplos de Cenários de Teste

Crie testes simples para validar o Edu:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação este mês?"
- **Resposta esperada:** R$ 470 (baseado em transacoes.csv: supermercado + restaurante)
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para minha reserva de emergência?"
- **Resposta esperada:** Tesouro Selic ou CDB (baixo risco, compatível com perfil moderado)
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo hoje?"
- **Resposta esperada:** Admitir especialização em finanças e oferecer ajuda relacionada
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o Fundo Multimercado?"
- **Resposta esperada:** Admitir não ter dados exatos e sugerir verificar fontes oficiais
- **Resultado:** [ ] Correto  [ ] Incorreto

### Teste 5: Acompanhamento de metas
- **Pergunta:** "Como estou indo com minha meta de reserva?"
- **Resposta esperada:** Atual R$ 10.000 de R$ 15.000, progresso e sugestões
- **Resultado:** [ ] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- [Liste aqui]

**O que pode melhorar:**
- [Liste aqui]

---

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Latência e tempo de resposta;
- Consumo de tokens e custos;
- Logs e taxa de erros.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!