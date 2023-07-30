from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'w83aJSWWfVLzE6'
app.config['MYSQL_DB'] = 'usuarios_spotify'

mysql = MySQL(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO usuarios (usuario, contrasena) VALUES (%s, %s)", (usuario, contrasena))
        mysql.connection.commit()
        cur.close()

        registrado = True  # Variable para indicar registro exitoso

        return redirect('/inicio_sesion?registrado=true')

    return render_template('registro.html')


@app.route('/inicio_sesion', methods=['GET', 'POST'])
def inicio_sesion():
    registrado = request.args.get('registrado')  # Obtener el valor de la variable registrado

    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM usuarios WHERE usuario = %s AND contrasena = %s", (usuario, contrasena))
        usuario_encontrado = cur.fetchone()
        cur.close()

        if usuario_encontrado:
            # Iniciar sesión exitosa
            # Realiza las acciones necesarias, como establecer una sesión
            return redirect('/inicio')
        else:
            # Credenciales incorrectas
            return "Credenciales incorrectas"

    return render_template('inicio_sesion.html', registrado=registrado)


if __name__ == '__main__':
    app.run(debug=True)
