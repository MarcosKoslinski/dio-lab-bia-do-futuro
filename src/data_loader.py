import pandas as pd
import json
from config import TRANSACOES_FILE, PERFIL_FILE, PRODUTOS_FILE, HISTORICO_FILE

def load_transacoes():
    df = pd.read_csv(TRANSACOES_FILE)
    # Agregar totais por categoria
    totais = df.groupby('categoria')['valor'].sum().to_dict()
    return df, totais

def load_perfil():
    with open(PERFIL_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_produtos():
    with open(PRODUTOS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_historico():
    df = pd.read_csv(HISTORICO_FILE)
    return df

def format_contexto(perfil, produtos, totais_transacoes, historico):
    contexto = f"""
Dados do Cliente:
- Nome: {perfil['nome']}
- Idade: {perfil['idade']}
- Profissão: {perfil['profissao']}
- Renda Mensal: R$ {perfil['renda_mensal']}
- Perfil de Investidor: {perfil['perfil_investidor']}
- Objetivo Principal: {perfil['objetivo_principal']}
- Metas: {', '.join([f"{m['meta']} (R$ {m['valor_necessario']})" for m in perfil['metas']])}

Resumo de Transações:
- Receitas Totais: R$ {totais_transacoes.get('receita', 0)}
- Despesas Totais: R$ {sum(v for k, v in totais_transacoes.items() if k != 'receita')}

Produtos Disponíveis: {', '.join([p['nome'] for p in produtos])}
"""
    return contexto