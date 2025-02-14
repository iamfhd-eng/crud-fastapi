from fastapi import APIRouter
from src.controllers.employee_controller import router as employee_controller_router

router = APIRouter()
router.include_router(employee_controller_router, prefix="/employees", tags=["employees"])
