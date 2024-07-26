from fastapi import APIRouter
from ..routers import student
router = APIRouter(prefix="/v1")
router.include_router(student.router)
