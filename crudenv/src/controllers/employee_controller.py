from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.services.employee_service import create_employee, get_employees, get_employee_by_id, update_employee, delete_employee
from src.database import config
from src.database.config import SessionLocal  # Correct import path
from src.schemas.employee_schema import EmployeeCreate, EmployeeOut

router = APIRouter()


@router.post("/", response_model=EmployeeOut)
def create_employee_route(employee: EmployeeCreate, db: Session = Depends(SessionLocal)):
    # Create the employee in the database
    db_employee = create_employee(db, employee.name, employee.position, employee.department)
    return db_employee



# Get all employees
@router.get("/", response_model=list[EmployeeOut])
def get_employees_route(skip: int = 0, limit: int = 10, db: Session = Depends(config.SessionLocal)):
    return get_employees(db, skip, limit)

# Get employee by ID
@router.get("/{employee_id}", response_model=EmployeeOut)
def get_employee_route(employee_id: int, db: Session = Depends(config.SessionLocal)):
    db_employee = get_employee_by_id(db, employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

# Edit Employee
@router.put("/{employee_id}", response_model=EmployeeOut)
def edit_employee_route(employee_id: int, employee: EmployeeCreate, db: Session = Depends(config.SessionLocal)):
    db_employee = update_employee(db, employee_id, employee.name, employee.position, employee.department)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

# Delete Employee
@router.delete("/{employee_id}", response_model=EmployeeOut)
def delete_employee_route(employee_id: int, db: Session = Depends(config.SessionLocal)):
    db_employee = delete_employee(db, employee_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee
