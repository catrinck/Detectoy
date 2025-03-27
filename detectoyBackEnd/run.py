import os
from dotenv import load_dotenv
import uvicorn
from app.main import app

# Carrega variáveis de ambiente
load_dotenv()

# Cria diretórios necessários se não existirem
os.makedirs('app/static/detections', exist_ok=True)
os.makedirs('app/static/results', exist_ok=True)
os.makedirs('models', exist_ok=True)

# Verifica se o arquivo do modelo existe
model_path = os.getenv('MODEL_PATH', 'models/thebest.pt')
if not os.path.exists(model_path):
    print(f"AVISO: O arquivo do modelo não foi encontrado em {model_path}")
    print("Por favor, certifique-se de que o arquivo do modelo está presente no diretório models/")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8080, reload=True) 