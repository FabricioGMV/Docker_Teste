import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Criar tabela de clientes
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    cidade TEXT
)
""")

# Criar tabela de vendas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    valor REAL,
    data TEXT,
    FOREIGN KEY(cliente_id) REFERENCES clientes(id)
)
""")

# Inserir dados de exemplo
cursor.execute("DELETE FROM clientes")
cursor.execute("DELETE FROM vendas")

clientes = [("Paulo Silva", "paulo@email.com", "São Paulo"),
            ("Ana Maria", "ana@email.com", "Rio de Janeiro"),
            ("Carlos Souza", "carlos@email.com", "Belo Horizonte")]

cursor.executemany("INSERT INTO clientes (nome, email, cidade) VALUES (?, ?, ?)", clientes)

vendas = [(1, 1500.0, "2025-10-01"),
          (2, 2300.0, "2025-10-02"),
          (3, 1200.0, "2025-10-05"),
          (1, 800.0, "2025-10-10")]

cursor.executemany("INSERT INTO vendas (cliente_id, valor, data) VALUES (?, ?, ?)", vendas)

conn.commit()
conn.close()
print("Banco criado com sucesso!")
