from data.cliente_model import Cliente
from data.cliente_sql import *
from data.util import get_connection

def criar_tabela():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(CRIAR_TABELA)
    conn.commit()
    conn.close()

def inserir_cliente(cliente):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(INSERIR_CLIENTE, (cliente.Nome, cliente.CPF, cliente.Email, cliente.Telefone, cliente.Senha))
    conn.commit()
    conn.close()

def obter_todos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(OBTER_TODOS)
    clientes = cursor.fetchall()
    clientes = [Cliente (id=row[0], Nome=row[1], CPF=row[2], Email=row[3], Telefone=row[4], Senha=row[5]) for row in clientes]
    conn.close()
    return clientes
