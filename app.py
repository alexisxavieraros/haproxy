from flask import Flask, render_template
from urllib.parse import quote
import os

app = Flask(__name__)

def read_haproxy_conf():
    haproxy_conf_path = '/app/haproxy.conf'
    if os.path.exists(haproxy_conf_path):
        with open(haproxy_conf_path, 'r') as file:
            content = file.read()
            return content
    else:
        return "El archivo haproxy.conf no se encuentra."

def process_haproxy_conf(content):
    # Aquí deberías agregar la lógica para procesar el contenido del archivo
    # y extraer información específica sobre solicitudes, rendimiento, y URL.
    # Este es solo un ejemplo básico, y necesitarás ajustarlo según el formato real del archivo.

    # Supongamos que el contenido tiene líneas que comienzan con 'URL:', 'Requests:', y 'Performance:'
    url_list = [line.split(':', 1)[1].strip() for line in content.split('\n') if line.startswith('URL:')]
    requests_data = [line.split(':', 1)[1].strip() for line in content.split('\n') if line.startswith('Requests:')]
    performance_data = [line.split(':', 1)[1].strip() for line in content.split('\n') if line.startswith('Performance:')]

    return {'url_list': url_list, 'requests_data': requests_data, 'performance_data': performance_data}

@app.route('/')
def index():
    haproxy_content = read_haproxy_conf()
    data = process_haproxy_conf(haproxy_content)
    return render_template('dashboard.html', data=data)

