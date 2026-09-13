"""
MatchMind Backend — FastAPI
Fase 0: Servidor mínimo
"""

from fastapi import FastAPI
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

app = FastAPI(
    title="MatchMind Backend",
    version="0.1.0",
    description="API backend para análise de apostas desportivas com IA"
)


@app.get("/")
async def root():
    """Health check — verifica se o servidor está online"""
    return {
        "status": "ok",
        "service": "matchmind-backend",
        "phase": "0"
    }


@app.get("/health")
async def health():
    """Endpoint para keep-alive (UptimeRobot vai usar isto)"""
    return {"status": "healthy"}


@app.get("/config")
async def config():
    """Debug: mostra variáveis carregadas (sem expor valores)"""
    return {
        "supabase_url": "configured" if os.getenv("SUPABASE_URL") else "missing",
        "gemini_model": os.getenv("GEMINI_MODEL"),
        "phase": "0 — não há endpoints de análise ainda"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
