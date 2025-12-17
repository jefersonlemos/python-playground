from fastapi import FastAPI
from finance_api.api.v1 import router as v1_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="Finance API",
        description="API for finance-related operations",
        version="0.1.0",
        openapi_tags=[
            {
                "name": "system",
                "description": "System and health-related endpoints",
            }
        ],
    )
    app.include_router(v1_router)
    return app

app = create_app()
