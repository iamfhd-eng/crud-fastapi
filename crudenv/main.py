from fastapi import FastAPI
from src.routes.employee_routes import router as employee_router
from src.database import config

app = FastAPI()

app.include_router(employee_router)

@app.on_event("startup")
async def startup():
    config.connect_db()

@app.on_event("shutdown")
async def shutdown():
    config.disconnect_db()
