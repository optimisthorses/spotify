from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Ruta de inicio
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Ruta de registro
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        # Aquí puedes agregar la lógica para guardar los datos en la base de datos

        # Redireccionar a la página de inicio de sesión con mensaje de registro exitoso
        return redirect('/inicio_sesion?registro=exitoso')

    return render_template('registro.html')

# Ruta de inicio de sesión
@app.route('/inicio_sesion', methods=['GET', 'POST'])
def inicio_sesion():
    # Verificar si se pasó un mensaje de registro exitoso en la URL
    registro_exitoso = request.args.get('registro')

    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        # Aquí puedes agregar la lógica para autenticar los datos en la base de datos
        if usuario == 'usuario' and contrasena == 'contrasena':
            # Iniciar sesión exitosa
            return redirect('/inicio?login=exitoso')
        else:
            # Credenciales incorrectas
            return redirect('/inicio_sesion?login=fallido')

    return render_template('inicio_sesion.html', registro_exitoso=registro_exitoso)

# Ruta de inicio de sesión exitoso
@app.route('/inicio', methods=['GET'])
def inicio():
    # Verificar si se pasó un mensaje de inicio de sesión exitoso en la URL
    login_exitoso = request.args.get('login')

    return render_template('inicio.html', login_exitoso=login_exitoso)


if __name__ == '__main__':
    app.run(debug=True)
