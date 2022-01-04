import os
import asyncio
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from elasticsearch_dsl import connections

from .router import person
from .router import health
from .api import indices

logging_conf = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logging.conf')
logging.config.fileConfig(logging_conf, disable_existing_loggers=False)
logger = logging.getLogger(__name__)

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
    max_tries = 100
    n_tries = 0

    while n_tries < max_tries:
        try:
            connections.create_connection(hosts=[es_host], timeout=20)
            indices.Person.init()

            logger.debug(f'initalized elasticsearch with n_tries={n_tries}')

            break
        except:
            logger.debug(f'failed to initialize elasticsearch with n_tries={n_tries} of max_tries={max_tries}')
            await asyncio.sleep(5)
        finally:
            n_tries += 1
