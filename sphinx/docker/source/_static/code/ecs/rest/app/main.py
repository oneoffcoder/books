import os
import asyncio

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from elasticsearch_dsl import connections

from .router import person
from .router import health
from .api import indices

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

@app.on_event('startup')
async def init_search():
    es_host = os.getenv('ES_HOST', 'localhost:9200')
    n_tries = 0

    while n_tries < 100:
        try:
            connections.create_connection(hosts=[es_host], timeout=20)
            indices.Person.init()

            break
        except:
            await asyncio.sleep(5)
        finally:
            n_tries += 1
