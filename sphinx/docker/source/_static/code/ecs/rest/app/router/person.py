from fastapi import APIRouter

router = APIRouter(tags=['person'])

@router.get('/v1/person', summary='Get person.')
def health():
    return {
        'status': 'ok',
        'type': 'person'
    }