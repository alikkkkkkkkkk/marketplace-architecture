from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Catalog Service",
    description="Catalog service skeleton for marketplace architecture homework",
    version="0.1.0",
)


@app.get("/health", status_code=200)
async def health() -> JSONResponse:
    return JSONResponse(
        status_code=200,
        content={
            "status": "ok",
            "service": "catalog-service",
        },
    )
