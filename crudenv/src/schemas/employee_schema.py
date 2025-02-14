from pydantic import BaseModel

# This is used for the request body (creating employee)
class EmployeeCreate(BaseModel):
    name: str
    position: str
    department: str

    class Config:
        orm_mode = True  # This allows conversion between Pydantic and SQLAlchemy models

# This is used for the response (returning created employee data)
class EmployeeOut(EmployeeCreate):
    id: int

    class Config:
        orm_mode = True  # Same as above, but including `id` for the response
