from fastapi import FastAPI
from app.routes import predict

app = FastAPI(title="Health Analytics AI Service", version="1.0.0")

app.include_router(predict.router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "OK"}
