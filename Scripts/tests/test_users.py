from fastapi import FastAPI
import pytest
from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.database import get_db, Base

#SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:wyzecam53$DELMY@localhost/sakila"

SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:wyzecam53@206.189.228.195/fastapi"


#SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

Base = declarative_base()

# Dependency
#def override_get_db():
    #db = TestingSessionLocal()
    #try:
       # yield db
    #finally:
       # db.close()



@pytest.fixture
def session():
	Base.metadata.drop_all(bind=engine)
	Base.metadata.create_all(bind=engine)
	db = TestingSessionLocal()
	try:
		yield db
	finally:
		db.close()



@pytest.fixture
def client(session):
	#run our code before we run our test
	def override_get_db():
		try:
			yield session
		finally:
			session.close()
	app.dependency_overrides[get_db] = override_get_db
	yield TestClient(app)
	#run our code after our test finishes

def test_root(client):
	res = client.get("/")
	print(res.json().get('message'))
	assert res.json().get('message') == "Frankley's API message!!! from ubuntu sort off"
	assert res.status_code == 200

def test_create_user(client):
	res = client.post("/users/", json = {"email":"frankley@gmail.com", "password":"frankley"}
		)
	print(res.json())
	assert res.status_code == 201