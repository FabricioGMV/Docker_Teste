
import mysql.connector
from mysql.connector import Error

# Configurações de conexão
servername = "db"  # Nome do serviço MySQL no docker-compose
username = "root"
password = "Senha123"
database = "testedb"

try:
    # Criar conexão com o banco de dados
    connection = mysql.connector.connect(
        host=servername,
        user=username,
        password=password,
        database=database
    )
    
    if connection.is_connected():
        print(f"Conectado ao banco de dados {database}!")
        
        cursor = connection.cursor()
        
        # Executar a consulta
        query = "SELECT * FROM tabela_exemplo"
        cursor.execute(query)
        
        # Buscar e exibir os resultados
        results = cursor.fetchall()
        for row in results:
            print(f"Nome: {row[0]}, Cidade: {row[1]}, Salário: {row[2]}")
    
except Error as e:
    print(f"Erro ao conectar ou consultar o banco de dados: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexão com o banco de dados fechada.")
