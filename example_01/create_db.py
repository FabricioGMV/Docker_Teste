import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Criar tabela de clientes (empresas)
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

# Limpar dados antigos
cursor.execute("DELETE FROM clientes")
cursor.execute("DELETE FROM vendas")

# Inserir empresas fictícias premium
clientes = [
    ("TechNova Solutions", "contato@technova.com", "São Paulo"),
    ("GlobalBank Corp", "comercial@globalbank.com", "Rio de Janeiro"),
    ("SkyNet Systems", "vendas@skynet.io", "Curitiba"),
    ("NeoLogix Industries", "info@neologix.com", "Belo Horizonte"),
    ("CloudWorks Ltda", "suporte@cloudworks.com", "Porto Alegre")
]

cursor.executemany("INSERT INTO clientes (nome, email, cidade) VALUES (?, ?, ?)", clientes)

# Inserir vendas associadas às empresas
vendas = [
    (1, 15000.0, "2025-10-01"),
    (2, 23000.0, "2025-10-03"),
    (3, 18000.0, "2025-10-07"),
    (4, 12500.0, "2025-10-12"),
    (5, 9500.0, "2025-10-15"),
    (1, 8700.0, "2025-10-20"),
    (2, 19200.0, "2025-10-22"),
    (3, 14200.0, "2025-10-25"),
    (4, 21000.0, "2025-10-27"),
    (5, 16000.0, "2025-10-30")
]

cursor.executemany("INSERT INTO vendas (cliente_id, valor, data) VALUES (?, ?, ?)", vendas)

conn.commit()
conn.close()
print("Banco criado e populado com sucesso!")
