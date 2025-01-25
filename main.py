import mysql.connector as mysql
from tabulate import tabulate

try:
  db = mysql.connect(
    host='localhost',   
    port=3306,
    user='root',
    password='',
    database='estoque'
)

except:
  print("\033[31m Erro ao conectar ao banco de dados. Por favor tente novamente\033[m")
  
else:
  print("\033[32mConexão com o banco estabelecida com sucesso \033[m!")

cursor = db.cursor()

def regitrar_venda():
    pass


def inserir_produto():
    nome = input("Nome do produto: ")
    descricao = input("descrição do produto: ")
    quantidade_disponivel = int(input("Quantidade inicial em estoque: "))
    preco = float(input('preço do produto: '))
    
    cursor.execute(
        "INSERT INTO produto (nome, descricao, quantidade_disponivel, preco) VALUES (%s, %s, %s, %s)",
        (nome, descricao, quantidade_disponivel, preco)
    )
    db.commit()
    print("\033[32mProduto inserido com sucesso!\033[m")


def excluir_produto():
    produto_id = int(input("ID do produto a excluir: "))
    cursor.execute("DELETE FROM produto WHERE id = %s", (produto_id,))
    db.commit()
    print("\033[32mProduto excluído com sucesso!\033[m")


def consultar_produtos():
  cursor.execute("SELECT * FROM produto;")
  res = cursor.fetchall()
  print(tabulate(res))

def consultar_vendas():
  cursor.execute("SELECT * FROM vendas;")
  res = cursor.fetchall()
  print(tabulate(res))

  

def menu():
  print("="*30)
  print("Menu".center(30))
  print("="*30)
  print("1 - Consultar estoque")
  print("2 - Inserir novo produto")
  print("3 - Registrar Venda")
  print("4 - Excluir Produto")
  print("5 - Atualizar produto")
  opc:int = int(input("-> "))
  return opc

def main():
  opcao = menu()
  if opcao == 1:
    consultar_produtos()
  
  if opcao == 2:
    inserir_produto()
  
  if opcao == 3:
    regitrar_venda()
  
  if opcao == 4:
    excluir_produto()
  
  

if __name__ == "__main__":
  main()
