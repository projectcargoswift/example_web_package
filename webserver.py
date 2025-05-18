import os  
from flask import Flask, jsonify  

app = Flask(__name__)  

# Založte jednoduché routy  
@app.route('/')  
def index():  
    return jsonify({"message": "Vítejte na webovém serveru example_web_package!"})  

@app.route('/hello')  
def hello():  
    return jsonify({"message": "Ahoj, toto je odpověď ze serveru example_web_package!"})  

def register_commands(command_registry):  
    """Registruje příkazy pro hosting webové aplikace."""  
    command_registry['start-web-server'] = start_web_server  

def start_web_server(*args):  
    """Spouští webový server."""  
    host = '0.0.0.0'  
    port = 8000  
    print(f"Spouštím webový server na http://{host}:{port}...")  
    app.run(host=host, port=port, use_reloader=False)
