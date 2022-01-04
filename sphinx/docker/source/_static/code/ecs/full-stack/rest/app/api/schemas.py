from pydantic import BaseModel

class PersonBase(BaseModel):
    first_name: str
    last_name: str
    gender: str
    age: int


class PersonCreate(PersonBase):
    ...

class PersonUpdate(PersonBase):
    ...


class Person(PersonBase):
    id: int
    
    class Config:
        orm_mode = True

class Message(BaseModel):
    status: str
    content: str