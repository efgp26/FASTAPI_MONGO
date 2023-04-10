from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from app.server.database import *

from app.server.models.student import *

router = APIRouter()


@router.post("/", response_description="Student data added into the database")
async def add_student_data(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student(student)
    return response_model(new_student, "Student added successfully") 

