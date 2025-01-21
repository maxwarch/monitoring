from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()


@app.get("/")
def home():
    return "Hello World"

@app.get("/502")
def err502():
    raise HTTPException(status_code=502, detail="Item not found")

@app.get("/501")
def err500():
    raise HTTPException(status_code=500, detail="Item not found")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crée un endpoint /metric qui va écrire toutes les métriques
Instrumentator().instrument(app).expose(app)
