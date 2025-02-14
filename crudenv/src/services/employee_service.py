from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from src.database.models import Employee
from src.schemas.employee_schema import EmployeeCreate, EmployeeOut

def create_employee(db: Session, name: str, position: str, department: str) -> EmployeeOut:
    db_employee = Employee(name=name, position=position, department=department)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)  # Refresh to get the ID from the database
    
    return EmployeeOut(id=db_employee.id, name=db_employee.name, position=db_employee.position, department=db_employee.department)

def get_employees(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Employee).offset(skip).limit(limit).all()

def get_employee_by_id(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()

def update_employee(db: Session, employee_id: int, name: str, position: str, department: str):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if db_employee:
        db_employee.name = name
        db_employee.position = position
        db_employee.department = department
        db.commit()
        db.refresh(db_employee)
        return db_employee
    return None

def delete_employee(db: Session, employee_id: int):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
        return db_employee
    return None
