from typing import List

from fastapi import APIRouter
from fastapi import Query, Depends, Body, HTTPException

from ..api import schemas, service
from ..api.dependency import get_person_service

router = APIRouter(tags=['person'])


@router.get(
    path='/v1/person/{person_id}',
    response_model=schemas.Person,
    summary='Gets person by id.'
)
def read(
        person_id: int = Query(..., ge=0),
        person_service: service.PersonService = Depends(get_person_service)
):
    try:
        return person_service.read(person_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get(
    path='/v1/person',
    response_model=List[schemas.Person],
    summary='Gets a list of people.'
)
def read_all(
        skip: int = Query(0, ge=-1),
        limit: int = Query(10, ge=1, le=100),
        person_service: service.PersonService = Depends(get_person_service)
):
    try:
        return person_service.read_all(skip, limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post(
    path='/v1/person',
    response_model=schemas.Person,
    summary='Create a single person.'
)
def create(
        person: schemas.PersonCreate = Body(..., examples={
            'john_smith': {
                'summary': 'John Smith',
                'description': 'Insert John Smith into the data.',
                'value': {
                    'first_name': 'John',
                    'last_name': 'Smith',
                    'gender': 'M',
                    'age': 33
                }
            },
            'jane_robinson': {
                'summary': 'Jane Robinson',
                'description': 'Insert Jane Robinson into the data.',
                'value': {
                    'first_name': 'Jane',
                    'last_name': 'Robinson',
                    'gender': 'F',
                    'age': 34
                }
            }
        }),
        person_service: service.PersonService = Depends(get_person_service)
):
    try:
        return person_service.create(person)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put(
    path='/v1/person/{person_id}',
    response_model=schemas.Message,
    summary='Updates a single person.'
)
def update(
        person_id: int = Query(..., ge=0),
        person: schemas.PersonUpdate = Body(..., examples={
            'john_smith': {
                'summary': 'John Smith',
                'description': 'Updates John Smith in the data.',
                'value': {
                    'first_name': 'John',
                    'last_name': 'Smith',
                    'gender': 'M',
                    'age': 33
                }
            }
        }),
        person_service: service.PersonService = Depends(get_person_service)
):
    try:
        person_service.update(person_id, person)
        return schemas.Message(**{
            'status': 'ok',
            'content': 'Update completed.'
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete(
    path='/v1/person/{person_id}',
    response_model=schemas.Message,
    summary='Delete person by id.'
)
def delete(
        person_id: int = Query(..., ge=0),
        person_service: service.PersonService = Depends(get_person_service)
):
    try:
        person_service.delete(person_id)
        return schemas.Message(**{
            'status': 'ok',
            'content': 'Delete completed.'
        })
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
