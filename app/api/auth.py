from fastapi import APIRouter, Depends, HTTPException, status, Security
from fastapi.security import APIKeyHeader
from app.core.security import (
    create_access_token,
    decode_access_token,
    get_password_hash,
    verify_password
)
from app.schemas.auth import User, UserInDB, Token, UserLogin
from datetime import timedelta

router = APIRouter(
    prefix="/v1",
    tags=["Autenticação"]
)

# Configuração para ler o token no header
api_key_header = APIKeyHeader(name="Authorization")

# Usuário fixo (mock)
fake_user_db = {
    "admin": {
        "username": "admin",
        "hashed_password": get_password_hash("123456")
    }
}


def authenticate_user(username: str, password: str):
    user = fake_user_db.get(username)
    if not user:
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return UserInDB(**user)


def get_current_user(token: str = Security(api_key_header)):
    if token.lower().startswith("bearer "):
        token = token[7:]

    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado.",
        )
    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(status_code=401, detail="Token inválido")
    user = fake_user_db.get(username)
    if user is None:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    return User(**user)


@router.post("/token", response_model=Token)
def login_for_access_token(user_login: UserLogin):
    user = authenticate_user(user_login.username, user_login.password)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Usuário ou senha incorretos",
        )
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=timedelta(minutes=60)
    )
    return {"access_token": access_token, "token_type": "bearer"}
