from fastapi import APIRouter, HTTPException
from app.services import scraper
from fastapi import Depends
from app.api.auth import get_current_user
from app.schemas.auth import User

router = APIRouter(
    prefix="/v1",
    tags=["Vitibrasil"]
)


@router.get("/producao")
def get_producao(user: User = Depends(get_current_user)):
    """
    Retorna os dados da aba Produção.
    """
    try:
        df = scraper.get_data("producao")
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/processamento")
def get_processamento(user: User = Depends(get_current_user)):
    """
    Retorna os dados da aba Processamento.
    Requer autenticação JWT.
    """
    try:
        df = scraper.get_data("processamento")
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/comercializacao")
def get_comercializacao(user: User = Depends(get_current_user)):
    """
    Retorna os dados da aba Comercialização.
    """
    try:
        df = scraper.get_data("comercializacao")
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/importacao")
def get_importacao(user: User = Depends(get_current_user)):
    """
    Retorna os dados da aba Importação.
    """
    try:
        df = scraper.get_data("importacao")
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/exportacao")
def get_exportacao(user: User = Depends(get_current_user)):
    """
    Retorna os dados da aba Exportação.
    """
    try:
        df = scraper.get_data("exportacao")
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
