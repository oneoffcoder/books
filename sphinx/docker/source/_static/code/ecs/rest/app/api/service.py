from typing import List

from . import models, schemas, dao

class PersonService:
    def __init__(self, dao: dao.PersonDao):
        self.__dao = dao

    @staticmethod
    def __convert(p: models.Person) -> schemas.Person:
        return schemas.Person(**{
            'id': p.id,
            'first_name': p.first_name,
            'last_name': p.last_name,
            'gender': p.gender,
            'age': p.age
        })

    def read(self, person_id: int) -> schemas.Person:
        return PersonService.__convert(self.__dao.read(person_id))
    
    def read_all(self, skip: int = 0, limit: int = 100) -> List[schemas.Person]:
        return [PersonService.__convert(p) for p in self.__dao.read_all(skip, limit)]

    def create(self, person: schemas.PersonCreate) -> schemas.Person:
        return PersonService.__convert(self.__dao.create(person))

    def update(self, person_id: int, person: schemas.PersonUpdate) -> None:
        self.__dao.update(person_id, person)

    def delete(self, person_id: int) -> None:
        self.__dao.delete(person_id)
