import os
from dotenv import load_dotenv
import uvicorn
from app.main import app

# Carrega as variáveis de ambiente
load_dotenv()

if __name__ == "__main__":
    # Cria os diretórios necessários se não existirem
    os.makedirs("app/static/detections", exist_ok=True)
    os.makedirs("results", exist_ok=True)
    
    # Inicia o servidor
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    ) 