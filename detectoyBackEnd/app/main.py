from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from .routers import detections, users, authentication, reports, webcam, websocket
from .routes import user_routes, auth_routes
from .database import engine, Base, get_db
from sqlalchemy.orm import Session
import logging

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cria as tabelas no banco de dados
try:
    Base.metadata.create_all(bind=engine)
    logger.info("Tabelas criadas com sucesso no banco de dados")
except Exception as e:
    logger.error(f"Erro ao criar tabelas no banco de dados: {str(e)}")

app = FastAPI(
    title="Detectoy API",
    description="API para detecção de defeitos em maquininhas",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint de saúde para verificar a conexão com o banco de dados
@app.get("/health")
async def health_check(db: Session = Depends(get_db)):
    try:
        # Testa a conexão com o banco de dados
        db.execute("SELECT 1")
        return {"status": "ok", "database": "connected"}
    except Exception as e:
        logger.error(f"Erro ao verificar a saúde da API: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro na conexão com o banco de dados: {str(e)}")

# Routers - todas as rotas com prefixo /api/v1
app.include_router(
    detections.router,
    prefix="/api/v1",
    tags=["detections"]
)

app.include_router(
    users.router,
    prefix="/api/v1",
    tags=["users"]
)

app.include_router(
    authentication.router,
    prefix="/api/v1",
    tags=["auth"]
)

app.include_router(
    reports.router,
    prefix="/api/v1",
    tags=["reports"]
)

app.include_router(
    webcam.router,
    prefix="/api/v1",
    tags=["webcam"]
)

app.include_router(
    websocket.router,
    tags=["websocket"]
)

# Configuração dos arquivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def root():
    """Retorna a página de documentação HTML"""
    return FileResponse('app/static/html/index.html', media_type='text/html')