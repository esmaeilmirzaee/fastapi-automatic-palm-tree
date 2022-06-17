from fastapi import FastAPI
from .models import User, Gender, Role
from typing import List
from uuid import uuid4


app = FastAPI()

db: List[User] = [
    User(id=uuid4(), first_name='Jane', last_name='DOE', gender=Gender.female, roles=[Role.user, Role.admin]),
    User(id=uuid4(), first_name='John', last_name='DOE', gender=Gender.female, roles=[Role.student])
]


@app.get('/')
def root():
    return {"message": "Hello World"}
