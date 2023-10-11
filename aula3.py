import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, inspect, text

url_itens_pedidos = 'https://github.com/alura-cursos/SQL-python-integracao/raw/main/TABELAS/itens_pedidos.csv'
url_pedidos = 'https://github.com/alura-cursos/SQL-python-integracao/raw/main/TABELAS/pedidos.csv'
url_produto = 'https://github.com/alura-cursos/SQL-python-integracao/raw/main/TABELAS/produtos.csv'
url_vendedores = 'https://github.com/alura-cursos/SQL-python-integracao/raw/main/TABELAS/vendedores.csv'

def pula_linha():
    print("\n")

itens_pedidos = pd.read_csv(url_itens_pedidos)
pedidos = pd.read_csv(url_pedidos)
produtos = pd.read_csv(url_produto)
vendedores = pd.read_csv(url_vendedores)

engine = create_engine('sqlite:///:memory:')

produtos.to_sql('produtos', engine, index=False)
itens_pedidos.to_sql('itens_pedidos', engine, index=False)
pedidos.to_sql('pedidos', engine, index=False)
vendedores.to_sql('vendedores', engine, index=False)

inspector = inspect(engine)
#print(inspector.get_table_names())

query = 'SELECT CONDICAO FROM PRODUTOS'

with engine.connect() as  conexao:
    consulta = conexao.execute(text(query))
    dados = consulta.fetchall()

pd.DataFrame(dados,columns=consulta.keys())

def sql_df(query):
    with engine.connect() as  conexao:
        consulta = conexao.execute(text(query))
        dados = consulta.fetchall()

    return pd.DataFrame(dados,columns=consulta.keys())


pula_linha()
query = '''SELECT CONDICAO, COUNT(*) AS 'Quantidade'
FROM PRODUTOS 
GROUP BY CONDICAO;'''

df_produtos = sql_df(query)
#print(df_produtos)

plt.bar(df_produtos['Condicao'],df_produtos['Quantidade'],  color='#9353FF')
plt.title('Contagem por tipo de condições dos produtos')
#plt.show() # visualizar o gráfico

pula_linha()
#print(sql_df('SELECT * FROM PRODUTOS').head(3))
pula_linha()
#print(sql_df('SELECT * FROM ITENS_PEDIDOS').head(3))

query = '''SELECT PRODUTOS.PRODUTO, SUM(ITENS_PEDIDOS.QUANTIDADE) As Quantidade
FROM ITENS_PEDIDOS, PRODUTOS
WHERE ITENS_PEDIDOS.PRODUTO_ID = PRODUTOS.PRODUTO_ID
GROUP BY PRODUTOS.PRODUTO
ORDER BY Quantidade ASC'''

#ASC ordem crescente DESC ordem decrescente

pula_linha()
df_prod_quant = sql_df(query)
#print(df_prod_quant)

#plt.figure(figsize=(10, 6))
plt.barh(df_prod_quant['produto'][-10:], df_prod_quant['Quantidade'][-10:], color='#9353FF')
plt.xlabel('Quantidade vendida')
#plt.show()

# 3. Lidando com Filtros

sql_df('SELECT * FROM PEDIDOS').head(3)
pula_linha()
sql_df('SELECT * FROM PEDIDOS').info(3)

query = '''SELECT VENDEDOR_ID, COUNT(*)
FROM  PEDIDOS
WHERE strftime('%Y',data_compra) = '2020'
GROUP BY VENDEDOR_ID;
'''

print(sql_df(query))

## Selecionar dados do ano de 2019
query = '''
SELECT strftime('%m', data_compra) AS mes, COUNT(*) AS quantidade_vendas
FROM pedidos
WHERE strftime('%Y', data_compra) = '2019'
GROUP BY mes;
'''
vendas_19 = sql_df(query)

## Selecionar dados do ano de 2020
query = '''
SELECT strftime('%m', data_compra) AS mes, COUNT(*) AS quantidade_vendas
FROM pedidos
WHERE strftime('%Y', data_compra) = '2020'
GROUP BY mes;
'''
vendas_20 = sql_df(query)

# Plotar o gráfico de 2019 e 2020
#plt.figure(figsize=(5, 3))
plt.plot(vendas_19.mes.to_numpy(), vendas_19.quantidade_vendas.to_numpy(), marker='o', linestyle='-', color='#9353FF', label = '2019')
plt.plot(vendas_20.mes.to_numpy(), vendas_20.quantidade_vendas.to_numpy(), marker='o', linestyle='-', color='#C0ED22', label = '2020')

# Definir título e eixos
plt.title('Vendas em 2019 e 2020')
plt.xlabel('Meses')
plt.ylabel('Quantidade de Vendas')

# Adicionar a legenda
plt.legend()

# Adicionar grid horizontal
plt.grid(axis='y', linestyle='--')

# Exibir a figura
#plt.show()




