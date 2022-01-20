import logging
from typing import List

from . import models, schemas, dao

logger = logging.getLogger(__name__)


class PersonService:
    def __init__(self, rdbms_dao: dao.RdbmsPersonDao):
        self.__rdbms_dao = rdbms_dao

    @staticmethod
    def __convert_m2s(p: models.Person) -> schemas.Person:
        return schemas.Person(**{
            'id': p.id,
            'first_name': p.first_name,
            'last_name': p.last_name,
            'gender': p.gender,
            'age': p.age
        })

    def read(self, person_id: int) -> schemas.Person:
        return PersonService.__convert_m2s(self.__rdbms_dao.read(person_id))

    def read_all(self, skip: int = 0, limit: int = 100) -> List[schemas.Person]:
        return [PersonService.__convert_m2s(p) for p in self.__rdbms_dao.read_all(skip, limit)]

    def create(self, person: schemas.PersonCreate) -> schemas.Person:
        m_person = self.__rdbms_dao.create(person)
        logger.debug(f'created person with id={m_person.id} in database')

        return PersonService.__convert_m2s(m_person)

    def update(self, person_id: int, person: schemas.PersonUpdate) -> None:
        self.__rdbms_dao.update(person_id, person)
        logger.debug(f'updated person with id={person_id} in database')

    def delete(self, person_id: int) -> None:
        self.__rdbms_dao.delete(person_id)
        logger.debug(f'deleted person with id={person_id} in database')
