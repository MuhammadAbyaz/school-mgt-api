from fastapi import APIRouter
from ..router import student
router = APIRouter(prefix="/v1")
router.include_router(student.router)
