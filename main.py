from fastapi import FastAPI
from models import User, Gender, Role
from typing import List
from uuid import UUID


app = FastAPI()

db: List[User] = [
    User(id=UUID("522e2967-75e4-48e9-a922-6805ca248e66"), first_name='Jane', last_name='DOE', gender=Gender.female, roles=[Role.user, Role.admin]),
    # User(id=UUID("2140e1c7-cd57-4544-8858-b3f7bc87ac1f"), first_name='John', last_name='DOE', gender=Gender.female,
    # roles=[Role.student])
]


@app.get('/')
def root():
    return {"message": "Hello World"}


@app.get('/api/v1/users')
async def fetch_users():
    return db


@app.post('/api/v1/users')
async def create_user(user: User):
    db.append(user)
    return {"message": "User created", 'user': user}


@app.delete('/api/v1/users/{user_id}')
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": "User deleted"}
    return {"message": "User not found"}
