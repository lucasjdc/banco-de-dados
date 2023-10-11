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
print(df_produtos)

plt.bar(df_produtos['Condicao'],df_produtos['Quantidade'],  color='#9353FF')
plt.title('Contagem por tipo de condições dos produtos')
#plt.show() // visualizar o gráfico

pula_linha()
print(sql_df('SELECT * FROM PRODUTOS').head(3))
pula_linha()
print(sql_df('SELECT * FROM ITENS_PEDIDOS').head(3))

query = '''SELECT PRODUTOS.PRODUTO, SUM(ITENS_PEDIDOS.QUANTIDADE) As Quantidade
FROM ITENS_PEDIDOS, PRODUTOS
WHERE ITENS_PEDIDOS.PRODUTO_ID = PRODUTOS.PRODUTO_ID
GROUP BY PRODUTOS.PRODUTO
ORDER BY Quantidade ASC'''

#ASC ordem crescente DESC ordem decrescente

pula_linha()
df_prod_quant = sql_df(query)
print(df_prod_quant)

plt.barh(df_prod_quant['produto'][-10:], df_prod_quant['Quantidade'][-10:], color='#9353FF')
plt.xlabel('Quantidade vendida')
plt.show()



