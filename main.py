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
  pass


def excluir_produto():
  pass


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
  print("4 - Atualizar produto")
  opc:int = int(input("-> "))
  return opc

def main():
  opcao = menu()
  if opcao == 1:
    consultar_produtos()
  
  if opcao == 2:
    pass
  
  if opcao == 3:
    pass
  
  if opcao == 4:
    pass
  
  

if "__name__" == "__main__":
  main()
