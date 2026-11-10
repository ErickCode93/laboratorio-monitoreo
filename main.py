from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Canal de Ventas FastAPI")

@app.get("/")
def home():
    return {"status": "Ventas Operando", "version": "v1-fastapi"}

@app.get("/comprar")
def comprar():
    return {"message": "Compra procesada exitosamente"}

# Esta línea expone la ruta /metrics para que Prometheus la lea
Instrumentator().instrument(app).expose(app)
