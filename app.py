# app.py

from flask import Flask, render_template

app = Flask(__name__)

# ... (tu código para procesar haproxy.conf y recopilar datos)

# Ruta para el dashboard
@app.route('/')
def index():
    # Devuelve el dashboard con las propiedades requeridas
    return render_template('dashboard.html', requests_data=requests_data, performance_data=performance_data, url_list=url_list)

# Si prefieres que el archivo se llame index.html, puedes cambiar el nombre del archivo a index.html y esta ruta a /index
@app.route('/dashboard')
def dashboard():
    # Similar al índice, puedes mantener esta ruta como /dashboard
    return render_template('dashboard.html', requests_data=requests_data, performance_data=performance_data, url_list=url_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
