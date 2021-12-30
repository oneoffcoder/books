from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .router import person
from .router import health

tags_metadata = [
    {'name': 'person', 'description': 'Person.'},
    {'name': 'health', 'description': 'Health.'}
]

app = FastAPI(
    title='Demo API',
    description='ECS demo API.',
    version='1.0.0',
    openapi_tags=tags_metadata
)

app.include_router(person.router)
app.include_router(health.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
