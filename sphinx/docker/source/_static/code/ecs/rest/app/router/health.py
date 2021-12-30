from fastapi import APIRouter

router = APIRouter(tags=['health'])

@router.get('/v1/health', summary='Health check.')
def health():
    return {
        'status': 'ok',
        'type': 'health'
    }