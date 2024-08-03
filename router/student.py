from fastapi import APIRouter,Request


from ..service.student import StudentService

router = APIRouter(prefix="/student")
student_service = StudentService()
@router.get("/",response_description="Returns all the students")
def get_students():
    return student_service.find_all()

@router.get("/{student_id}",response_description="Return a student with specific id")
def get_student_by_id(student_id:str):
    return student_service.find_by_id(student_id)
@router.post("/",response_description="Add new student and return its id")
async def create_student(request: Request):
    return student_service.insert(await request.json())
@router.put("/{student_id}",response_description="Update existing student and return its id")
async def update_student(student_id:str,request: Request):
    return student_service.update(student_id,await request.json())
