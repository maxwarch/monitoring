#https://signoz.io/guides/loguru/
from pathlib import Path
from fastapi import FastAPI, HTTPException, Request
from fastapi.concurrency import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

from custom_logging import CustomizeLogger
import logging

logger = logging.getLogger(__name__)
config_path=Path(__file__).with_name("logging_config.json")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    # print(loggers)

    logger = CustomizeLogger.make_logger(config_path)
    app.logger = logger
    
    yield
    pass


app = FastAPI(lifespan=lifespan)

@app.get("/")
def home():
    return "Hello World"

@app.get("/502")
def err502(req: Request):
    
    req.app.logger.debug('Debug 502')
    req.app.logger.error('Error 502')
    raise HTTPException(status_code=502, detail="Item not found")

@app.get("/500")
def err500(req: Request):
    logger.debug('Debug 500')
    logger.warning('Warning 500')
    logger.error('Error 500')
    raise HTTPException(status_code=500, detail="Item 500")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crée un endpoint /metric qui va écrire toutes les métriques
Instrumentator().instrument(app).expose(app)
