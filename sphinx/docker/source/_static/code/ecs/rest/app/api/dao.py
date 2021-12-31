from typing import List
from sqlalchemy.orm import Session
from elasticsearch_dsl import Search

from . import models, schemas, indices

class RdbmsPersonDao:
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
        self.__db.commit()
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

class SearchPersonDao:
    def read(self, person_id: int) -> indices.Person:
        return indices.Person.get(id=person_id)

    def read_all(self, skip: int = 0, limit: int = 100) -> List[indices.Person]:
        s = Search(index='person')
        s.update_from_dict({'from': skip, 'size': limit, 'query': {'match_all': {}}})

        hits = s.execute()
        return [indices.Person(meta={'id': h.meta.id}, **h.to_dict()) for h in hits]

    def create(self, person: schemas.Person) -> indices.Person:
        p = indices.Person(**{
            'meta': {'id': person.id},
            'first_name': person.first_name,
            'last_name': person.last_name,
            'gender': person.gender,
            'age': person.age
        })
        p.save()

        return self.read(person.id)

    def update(self, person_id: int, person: schemas.PersonUpdate) -> None:
        p = indices.Person(**{
            'meta': {'id': person_id},
            'first_name': person.first_name,
            'last_name': person.last_name,
            'gender': person.gender,
            'age': person.age
        })
        p.save()

    def delete(self, person_id: int) -> None:
        indices.Person.get(id=person_id).delete()