# Importa a classe FastAPI 
from fastapi import FastAPI

#cria a aplicação principal da API
app = FastAPI(
    title="ShadowTrap",
    description="SSH Honeypot & Threat Monitoring System",
    version="1.0.0"
)

# Rota principal da aplicação 
@app.get("/")
def home():

    #Retorna uma resposta em JSON
    return{
        "project": "Shadowtrap",
        "status": "online"
    }