from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import jwt

app = FastAPI(title="JWT Auth Example")
security = HTTPBearer()
SECRET_KEY = "demo-secret"
ALGORITHM = "HS256"

users = {"admin": "password123"}

tokens = {}


class LoginRequest(BaseModel):
    username: str
    password: str


@app.post("/login")
def login(data: LoginRequest):
    if users.get(data.username) != data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = jwt.encode({"sub": data.username}, SECRET_KEY, algorithm=ALGORITHM)
    tokens[data.username] = token
    return {"access_token": token, "token_type": "bearer"}


@app.post("/logout")
def logout(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    username = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])["sub"]
    tokens.pop(username, None)
    return {"message": "Logged out"}


@app.get("/protected")
def protected(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.PyJWTError as exc:
        raise HTTPException(status_code=401, detail="Invalid token") from exc

    if tokens.get(payload["sub"]) != token:
        raise HTTPException(status_code=401, detail="Token revoked")

    return {"message": f"Welcome {payload['sub']}"}
