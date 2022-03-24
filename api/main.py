from fastapi import FastAPI

from api.routes import healthcheck

app = FastAPI()

app.include_router(healthcheck.router)