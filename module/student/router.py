from fastapi import APIRouter


router = APIRouter(prefix="/student")

@router.get("/")
def helloWorld() -> str:
    return "Hello World"
