# app.py

from flask import Flask, render_template
from urllib.parse import quote
import os

app = Flask(__name__)

def read_haproxy_conf():
    haproxy_conf_path = '/app/haproxy.conf'  # Ruta al archivo haproxy.conf en el contenedor
    if os.path.exists(haproxy_conf_path):
        with open(haproxy_conf_path, 'r') as file:
            content = file.read()
            # Procesa el contenido del archivo haproxy.conf según tus necesidades
            # Aquí puedes extraer información, generar estadísticas, etc.
            return content
    else:
        return "El archivo haproxy.conf no se encuentra."

@app.route('/')
def index():
    haproxy_content = read_haproxy_conf()
    # Devuelve el dashboard con las propiedades requeridas y la información de haproxy.conf
    return render_template('dashboard.html', haproxy_content=haproxy_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
