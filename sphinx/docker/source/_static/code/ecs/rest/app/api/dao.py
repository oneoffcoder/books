from typing import List
from sqlalchemy.orm import Session

from . import models, schemas

class PersonDao:
    def __init__(self, db: Session):
        self.__db = db

    def read(self, person_id: int) -> models.Person:
        return self.__db\
            .query(models.Person)\
            .filter(models.Person.id == person_id)\
            .first()
    
    def read_all(self, skip: int = 0, limit: int = 100) -> List[models.Person]:
        return self.__db\
            .query(models.Person)\
            .offset(skip)\
            .limit(limit)\
            .all()

    def create(self, person: schemas.PersonCreate) -> models.Person:
        m_person = models.Person(**{
            'first_name': person.first_name,
            'last_name': person.last_name,
            'gender': person.gender,
            'age': person.age
        })

        self.__db.add(m_person)
        self.__db.flush()
        self.__db.refresh(m_person)

        return m_person

    def update(self, person_id: int, person: schemas.PersonUpdate) -> None:
        self.__db\
            .query(models.Person)\
            .filter(models.Person.id == person_id)\
            .update({
                'first_name': person.first_name,
                'last_name': person.last_name,
                'gender': person.gender,
                'age': person.age
            })
        self.__db.commit()

    def delete(self, person_id: int) -> None:
        self.__db\
            .query(models.Person)\
            .filter(models.Person.id == person_id)\
            .delete()
        self.__db.commit()

    

    