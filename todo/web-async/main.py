import asyncio
from random import randint, choice, random

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


@app.get('/number')
async def get_number():
    await asyncio.sleep(5)

    return {
        'number': randint(0, 10)
    }


@app.get('/color')
async def get_color():
    await asyncio.sleep(3)

    return {
        'color': choice(['red', 'green', 'blue'])
    }


@app.get('/probability')
async def get_probability():
    await asyncio.sleep(2)
    
    return {
        'probability': random()
    }
