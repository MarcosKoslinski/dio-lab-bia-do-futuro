# Base de Conhecimento

## Dados Utilizados

Os dados mockados na pasta `data/` alimentam o agente Edu, permitindo respostas personalizadas e insights financeiros baseados no perfil do usuário.

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores e histórico de atendimentos |
| `perfil_investidor.json` | JSON | Personalizar recomendações baseadas no perfil de risco e metas |
| `produtos_financeiros.json` | JSON | Sugerir produtos financeiros adequados ao perfil e objetivos |
| `transacoes.csv` | CSV | Analisar padrões de gastos e fornecer alertas ou insights |

---

## Como os Dados São Integrados

Os dados são processados para fornecer contexto relevante ao Edu, garantindo que as sugestões sejam personalizadas e baseadas em informações reais do usuário, como perfil de investimento e histórico de transações.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Idade: 32
- Profissão: Analista de Sistemas
- Renda Mensal: R$ 5.000,00
- Perfil de Investidor: Moderado
- Objetivo Principal: Construir reserva de emergência
- Patrimônio Total: R$ 15.000,00
- Reserva de Emergência Atual: R$ 10.000,00
- Aceita Risco: Não
- Metas: Completar reserva de emergência (R$ 15.000,00 até 2026-06); Entrada de apartamento (R$ 50.000,00 até 2027-12)

Resumo de Transações (último mês):
- Receitas Totais: R$ 5.000,00
- Despesas Totais: R$ 2.355,90
- Principais Categorias: Moradia (R$ 1.200,00), Alimentação (R$ 470,00), Saúde (R$ 154,00)

Produtos Financeiros Sugeridos (baseados no perfil):
- Tesouro Selic (Risco: Baixo, Indicado para reserva de emergência)
- CDB Liquidez Diária (Risco: Baixo, Indicado para segurança com rendimento diário)

Histórico de Atendimentos Recentes:
- 2025-10-01: Chat sobre Tesouro Selic - Explicação fornecida
- 2025-10-12: Chat sobre metas financeiras - Acompanhamento do progresso

Últimas transações:
- 2025-10-01: Salário - Entrada R$ 5.000,00
- 2025-10-02: Aluguel - Saída R$ 1.200,00
- 2025-10-03: Supermercado - Saída R$ 450,00
- 2025-10-05: Netflix - Saída R$ 55,90
```
