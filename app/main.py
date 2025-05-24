from fastapi import FastAPI
from app.api import endpoints, auth

app = FastAPI(
    title="VitiBrasil API",
    description="API para consulta de dados de vitivinicultura da Embrapa",
    version="1.0.0"
)

app.include_router(endpoints.router)
app.include_router(auth.router)


@app.get("/")
def read_root():
    return {"message": "VitiBrasil API is running"}
