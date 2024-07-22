from fastapi import APIRouter
from module.student.router import router as student_router


router = APIRouter(prefix="/v1")
router.include_router(student_router)
