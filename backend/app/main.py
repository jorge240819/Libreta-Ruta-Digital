from fastapi import FastAPI
from sqlalchemy import text
from app.db.session import engine

app = FastAPI(title="Libreta de Ruta API")

@app.get("/health")
def health():
    # Verificamos conexión a BD
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return {"status": "ok", "db": "ok"}
