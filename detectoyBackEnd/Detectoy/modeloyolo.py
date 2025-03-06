import cv2
import os
import psycopg2
import requests
import matplotlib.pyplot as plt
from pathlib import Path
from ultralytics import YOLO

# Configurações
CONFIDENCE_THRESHOLD = 0.35
MODEL_PATH = Path("detectoyBackEnd/Detectoy/models/best.pt")
IMAGE_DIR = Path("detectoyBackEnd/Detectoy/images")

# Configuração do banco de dados PostgreSQL
DB_CONFIG = {
    "dbname": "seu_banco",
    "user": "seu_usuario",
    "password": "sua_senha",
    "host": "localhost",  # ou IP do servidor PostgreSQL
    "port": "5432"
}

# Verificar se o modelo existe
if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Erro: O modelo {MODEL_PATH} não foi encontrado!")

print("Modelo encontrado!")

# Inicializar o modelo YOLO
model = YOLO(str(MODEL_PATH))

# Lista de imagens para processar
image_paths = [
    IMAGE_DIR / "img1.jpg",
    IMAGE_DIR / "img2.jpg",
    IMAGE_DIR / "img3.jpg",
    IMAGE_DIR / "img4.jpg"
]

# Criar diretório para resultados
output_dir = Path(f"{MODEL_PATH.stem}")
output_dir.mkdir(exist_ok=True)

def enviar_para_banco(image_path):
    """Envia a imagem para o banco de dados PostgreSQL."""
    try:
        with open(image_path, "rb") as img_file:
            image_data = img_file.read()

        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()

        query = "INSERT INTO imagens_defeituosas (imagem, nome_arquivo) VALUES (%s, %s);"
        cursor.execute(query, (image_data, image_path.name))

        connection.commit()
        cursor.close()
        connection.close()
        print(f"Imagem {image_path.name} enviada para o banco de dados.")
    except Exception as e:
        print(f"Erro ao enviar para o banco: {e}")

# Processar cada imagem
for idx, image_path in enumerate(image_paths, 1):
    print(f"Processando imagem {idx}/{len(image_paths)}: {image_path.name}")

    # Carregar a imagem
    image = cv2.imread(str(image_path))
    if image is None:
        print(f"Erro ao carregar {image_path}")
        continue

    # Fazer a inferência
    results = model(str(image_path), conf=CONFIDENCE_THRESHOLD)[0]

    # Desenhar caixas delimitadoras
    annotated_image = results.plot()

    # Mostrar a imagem com Matplotlib
    plt.figure(figsize=(10, 6))
    plt.imshow(cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()

    # Salvar resultado
    output_filename = output_dir / f"resultado_{MODEL_PATH.stem}_{image_path.name}"
    cv2.imwrite(str(output_filename), annotated_image)
    print(f"Resultado salvo em: {output_filename}")

    # Verificar se as classes 'tela quebrada' ou 'carcaca quebrada' foram detectadas
    detected_classes = [model.names[int(box.cls)] for box in results.boxes]
    if "tela_quebrada" in detected_classes or "carcaca_quebrada" in detected_classes:
        enviar_para_banco(output_filename)

print("\nProcessamento concluído!")