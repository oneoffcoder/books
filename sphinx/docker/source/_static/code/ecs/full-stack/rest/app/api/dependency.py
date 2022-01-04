from sqlalchemy.orm import Session
from . import database, dao, service

def get_db() -> Session:
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_rdbms_person_dao() -> dao.RdbmsPersonDao:
    return dao.RdbmsPersonDao(next(get_db()))

def get_search_person_dao() -> dao.SearchPersonDao:
    return dao.SearchPersonDao()

def get_person_service():
    return service.PersonService(
        get_rdbms_person_dao(),
        get_search_person_dao())