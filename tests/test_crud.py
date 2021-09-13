from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

from app import crud
from app.schemas import UserCreate
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session


def test_create_user(db: Session) -> None:
    email = "test@gmai.com"
    password = "testpassword"
    user_in = UserCreate(email=email, password=password)
    user = crud.user.create(db, obj_in=user_in)
    assert user.email == email
    assert hasattr(user, "password")