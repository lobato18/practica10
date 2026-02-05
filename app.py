import time
from flask import Flask
import redis

app = Flask(__name__)
# El host es el nombre del servicio en docker-compose
cache = redis.Redis(host='redis', port=6379)

@app.route('/')
def get_data():
    # Simulamos proceso pesado
    time.sleep(2) 
    return {"data": "Respuesta procesada", "timestamp": time.time()}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
