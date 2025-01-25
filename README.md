# Projeto: Gerenciamento de Estoque com MySQL e Tabulate

Este projeto conecta-se a um banco de dados MySQL chamado `estoque` e utiliza a biblioteca `tabulate` para exibir os dados das tabelas `produto` e `vendas` em formato tabular no terminal. Ele também fornece funcionalidades para gerenciar o estoque e registrar vendas por meio de um menu interativo.

## Requisitos

Antes de começar, certifique-se de ter instalado:

1. **Python** (versão 3.6 ou superior).
2. **MySQL** instalado e configurado.
3. As seguintes bibliotecas Python:
    - `mysql-connector-python`
    - `tabulate`

## Instalação das Bibliotecas

Use os comandos abaixo para instalar as bibliotecas necessárias:

```bash
pip install mysql-connector-python
pip install tabulate
```

## Estrutura do Banco de Dados

### Tabela `produto`

Certifique-se de que o banco de dados `estoque` e a tabela `produto` estão criados e populados. Um exemplo básico para criação:

```sql
CREATE DATABASE estoque;
USE estoque;

CREATE TABLE produto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    quantidade INT,
    preco DECIMAL(10, 2)
);

INSERT INTO produto (nome, quantidade, preco) VALUES
    ('Produto A', 10, 19.99),
    ('Produto B', 5, 29.99),
    ('Produto C', 20, 9.99);
```

### Tabela `vendas`

Além disso, crie a tabela `vendas` para registrar as vendas:

```sql
CREATE TABLE vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produto_id INT,
    quantidade INT,
    data_venda DATETIME,
    FOREIGN KEY (produto_id) REFERENCES produto(id)
);
```

## Código Principal

O código abaixo realiza a conexão com o banco de dados, exibe menus interativos e implementa funcionalidades como consulta de estoque, registro de vendas e gerenciamento de produtos:

```python
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

def registrar_venda():
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
```

## Funcionalidades Atuais

- **Consultar Estoque**: Lista todos os produtos no banco de dados.
- **Consultar Vendas**: Lista todas as vendas registradas.
- **Inserir Novo Produto**: (Em desenvolvimento)
- **Registrar Venda**: (Em desenvolvimento)
- **Excluir Produto**: (Em desenvolvimento)

## Execução

1. Certifique-se de que o servidor MySQL está em execução.
2. Execute o código Python no terminal:

```bash
python nome_do_arquivo.py
```

## Funcionalidades Futuras

- Finalizar funcionalidades para inserir, atualizar e deletar produtos no banco.
- Completar o registro de vendas e vinculação aos produtos.
- Criar uma interface gráfica para facilitar o gerenciamento.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias.

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).
