# Detectoy Backend

API FastAPI para detecção de defeitos em dispositivos móveis.

## Requisitos

- Python 3.8+
- PostgreSQL
- CUDA (opcional, para GPU)

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o banco de dados:
```bash
python db_setup.py
```

5. Configure as variáveis de ambiente:
- Copie o arquivo `.env.example` para `.env`
- Ajuste as variáveis conforme necessário

## Executando o servidor

```bash
python run.py
```

O servidor estará disponível em `http://localhost:8000`

## Documentação da API

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Endpoints

- `/api/v1/detections` - Detecção de imagens
- `/api/v1/camera/stream` - Stream de câmera
- `/api/v1/users` - Gerenciamento de usuários
- `/api/v1/auth` - Autenticação
- `/api/v1/reports` - Relatórios
