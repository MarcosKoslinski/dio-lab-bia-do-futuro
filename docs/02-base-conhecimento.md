# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores e histórico de atendimentos |
| `perfil_investidor.json` | JSON | Personalizar recomendações baseadas no perfil de risco e metas |
| `produtos_financeiros.json` | JSON | Sugerir produtos financeiros adequados ao perfil e objetivos |
| `transacoes.csv` | CSV | Analisar padrões de gastos e fornecer alertas ou insights |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados foram utilizados conforme fornecidos na pasta `data/`, sem modificações iniciais. Futuramente, podemos expandir o dataset com mais transações ou produtos para testar cenários adicionais, ou integrar dados públicos do Hugging Face para enriquecer a base de conhecimento.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos CSV e JSON são carregados no início da aplicação Python usando bibliotecas como Pandas (para CSV) e json (para JSON). Os dados são processados e armazenados em estruturas de dados (ex: DataFrames e dicionários) para acesso rápido durante a sessão.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados relevantes são incluídos dinamicamente no prompt enviado ao LLM via Ollama. Por exemplo, o perfil do investidor e produtos compatíveis são formatados e adicionados ao contexto do prompt para personalizar as respostas, garantindo que o agente responda com base em informações precisas.

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

Produtos Financeiros Sugeridos (baseados no perfil):
- Tesouro Selic (Risco: Baixo, Indicado para reserva de emergência)
- CDB Liquidez Diária (Risco: Baixo, Indicado para segurança com rendimento diário)

Últimas transações:
- 2025-10-01: Salário - Entrada R$ 5.000,00
- 2025-10-02: Aluguel - Saída R$ 1.200,00
- 2025-10-03: Supermercado - Saída R$ 450,00
- 2025-10-05: Netflix - Saída R$ 55,90
```
