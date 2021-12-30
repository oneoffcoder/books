from sqlalchemy.orm import Session
from . import database, dao, service

def get_db() -> Session:
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_person_dao() -> dao.PersonDao:
    return dao.PersonDao(get_db())

def get_person_service():
    return service.PersonService(get_person_dao())