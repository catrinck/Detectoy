from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from routers import detections, webcam, users, authentication, reports

app = FastAPI(
    title="Detectoy API",
    description="API for detecting broken screens and cases in devices"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(detections.router, prefix="/api/v1")
app.include_router(webcam.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")
app.include_router(authentication.router, prefix="/api/v1")
app.include_router(reports.router, prefix="/api/v1")

# Static files
app.mount("/static", StaticFiles(directory="src/static"), name="static")

@app.get("/")
async def root():
    return FileResponse('app/static/html/index.html')