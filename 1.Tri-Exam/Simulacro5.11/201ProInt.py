import mysql.connector
from flask import Flask

# Connect to MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="useroscar",
    password="Oscar081100!",
    database="PortafolioDB"
)

cursor = conexion.cursor()
app = Flask(__name__)

@app.route("/")                           # Ruta principal
def holamundo():                          
    cursor.execute("SELECT * FROM clientes;")   # Obtener datos
    filas = cursor.fetchall()
    print(filas)                                # Mostrar en terminal

    # Inicio HTML
    cadena = ''' 
    <!doctype html>
<html lang="es">
  <head>
    <title>Examen</title>
    <meta charset="utf-8">
    <style>
      html,body{background:grey;font-family:sans-serif;}
      header,main,footer{
        background:white;
        padding:20px;
        width:800px;
        margin:auto;
        text-align:center;
      }
      main{
        display:grid;
        grid-template-columns:auto auto auto;
        gap:20px;
      }
    </style>
  </head>
  <body>
    <header>
      <h1>Oscar Sørensen</h1>
      <h2>oscar@example.com</h2>
    </header>
    <main>
  '''

    # Parte repetitiva
    for fila in filas:
        cadena += f'''
      <article>
        <p>ID: {fila[0]}</p>
        <h3>{fila[1]} {fila[2]}</h3>
        <p>Email: {fila[3]}</p>
      </article>
    '''

    # Final HTML
    cadena += ''' 
    </main>
    <footer>
      (c) 2025 Oscar Sørensen
    </footer>
  </body>
</html>
  '''
    return cadena

if __name__ == "__main__":
    app.run(debug=True)
