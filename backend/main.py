"""
MatchMind Backend — FastAPI com teste de API-Football
Fase 0: Servidor mínimo + integração com API-Football
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import requests
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

app = FastAPI(
    title="MatchMind Backend",
    version="0.1.0",
    description="API backend para análise de apostas desportivas com IA"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Health check — verifica se o servidor está online"""
    return {
        "status": "ok",
        "service": "matchmind-backend",
        "phase": "0"
    }


# Aceita GET e HEAD para UptimeRobot
@app.api_route("/health", methods=["GET", "HEAD"])
async def health():
    """Endpoint para keep-alive (UptimeRobot)"""
    return {"status": "healthy"}


@app.get("/config")
async def config():
    """Debug: mostra variáveis carregadas (sem expor valores)"""
    return {
        "supabase_url": "configured" if os.getenv("SUPABASE_URL") else "missing",
        "gemini_model": os.getenv("GEMINI_MODEL"),
        "api_football_key": "configured" if os.getenv("API_FOOTBALL_KEY") else "missing",
        "phase": "0"
    }


@app.get("/test/api-football")
async def test_api_football():
    """
    Testa a conexão com API-Football
    Retorna as primeiras ligas disponíveis
    """
    api_key = os.getenv("API_FOOTBALL_KEY")

    if not api_key:
        return {
            "status": "error",
            "message": "API_FOOTBALL_KEY não configurada"
        }

    try:
        url = "https://v3.football.api-sports.io/leagues"
        headers = {
            "x-apisports-key": api_key
        }

        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code == 200:
            data = response.json()

            # Extrair primeiras 5 ligas
            leagues = []
            if "response" in data:
                for league_data in data["response"][:5]:
                    league = league_data.get("league", {})
                    leagues.append({
                        "id": league.get("id"),
                        "name": league.get("name"),
                        "country": league_data.get("country", {}).get("name")
                    })

            return {
                "status": "success",
                "message": "API-Football conectado com sucesso",
                "total_leagues": len(data.get("response", [])),
                "sample_leagues": leagues
            }
        else:
            return {
                "status": "error",
                "message": f"API-Football respondeu com status {response.status_code}",
                "details": response.text[:200]
            }

    except Exception as e:
        return {
            "status": "error",
            "message": f"Erro ao conectar com API-Football: {str(e)}"
        }


@app.get("/test/gemini")
async def test_gemini():
    """
    Testa a conexão com Google Gemini
    """
    api_key = os.getenv("GEMINI_API_KEY")
    model = os.getenv("GEMINI_MODEL")

    if not api_key or not model:
        return {
            "status": "error",
            "message": "GEMINI_API_KEY ou GEMINI_MODEL não configuradas"
        }

    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)

        client = genai.GenerativeModel(model)
        response = client.generate_content("Responde com uma palavra: MatchMind")

        if response.text:
            return {
                "status": "success",
                "message": "Gemini conectado com sucesso",
                "model": model,
                "response": response.text[:100]
            }
        else:
            return {
                "status": "error",
                "message": "Resposta vazia do Gemini"
            }

    except ImportError:
        return {
            "status": "error",
            "message": "google-generativeai não instalado"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Erro ao conectar com Gemini: {str(e)}"
        }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
