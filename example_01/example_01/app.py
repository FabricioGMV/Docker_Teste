from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
DB_NAME = "company.db"

@app.route("/")
def dashboard():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Buscar clientes
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()

    # Buscar vendas
    cursor.execute("""
        SELECT v.id, c.nome as cliente, v.valor, v.data 
        FROM vendas v
        JOIN clientes c ON v.cliente_id = c.id
    """)
    vendas = cursor.fetchall()

    # Preparar dados para gráficos
    cursor.execute("""
        SELECT c.nome, SUM(v.valor) as total
        FROM vendas v
        JOIN clientes c ON v.cliente_id = c.id
        GROUP BY c.nome
    """)
    vendas_por_cliente = cursor.fetchall()

    conn.close()

    return render_template("dashboard.html",
                       clientes=clientes,
                       vendas=vendas,
                       vendas_por_cliente=vendas_por_cliente)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
