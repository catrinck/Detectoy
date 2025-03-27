# Detectoy API

API para detecção de defeitos em telas de celular usando YOLO.

## Requisitos

- Python 3.8+
- PostgreSQL
- Modelo YOLO treinado (`thebest.pt`)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/detectoy.git
cd detectoy/detectoyBackEnd
```

2. Crie um ambiente virtual e ative-o:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o arquivo `.env`:
```bash
cp .env.example .env
```
Edite o arquivo `.env` com suas configurações.

5. Configure o banco de dados:
```bash
python db_setup.py
```

6. Coloque o modelo YOLO treinado na pasta `models/`:
```bash
mkdir -p models
# Copie o arquivo thebest.pt para a pasta models/
```

## Uso

1. Inicie o servidor:
```bash
python run.py
```

2. Acesse a documentação da API:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Endpoints

### Autenticação
- `POST /api/v1/token`: Login e obtenção do token JWT

### Usuários
- `POST /api/v1/users/`: Criar novo usuário
- `GET /api/v1/users/`: Listar usuários
- `GET /api/v1/users/{user_id}`: Obter usuário específico
- `PUT /api/v1/users/{user_id}`: Atualizar usuário
- `DELETE /api/v1/users/{user_id}`: Remover usuário

## Estrutura do Projeto

```
detectoyBackEnd/
├── app/
│   ├── models.py         # Modelos do banco de dados
│   ├── schemas.py        # Schemas Pydantic
│   ├── database.py       # Configuração do banco de dados
│   ├── main.py          # Aplicação FastAPI
│   ├── services/        # Serviços da aplicação
│   └── routes/          # Rotas da API
├── models/              # Modelos YOLO
├── static/             # Arquivos estáticos
├── .env                # Variáveis de ambiente
├── requirements.txt    # Dependências
└── run.py             # Script de inicialização
```

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
