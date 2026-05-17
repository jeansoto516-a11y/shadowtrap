# Importa a classe FastAPI 
from fastapi import FastAPI

# iMPORT THREADING
import threading

# importa honeypot 
from app.honeypot.ssh_server import start_ssh_honeypot

#cria a aplicação principal da API
app = FastAPI(
    title="ShadowTrap",
    description="SSH Honeypot & Threat Monitoring System",
    version="1.0.0"
)

honeypot_thread = threading.Thread(
    target=start_ssh_honeypot,
    daemon=True
)
honeypot_thread.start()

# Rota principal da aplicação 
@app.get("/")
def home():

    #Retorna uma resposta em JSON
    return{
        "project": "Shadowtrap",
        "status": "online"
    }