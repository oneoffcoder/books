from fastapi import APIRouter

router = APIRouter(tags=['misc'])

@router.get('/v1/health', summary='Health check.')
def health():
    return {
        'status': 'ok',
        'type': 'health'
    }