import time
from fastapi import FastAPI, Response,status,HTTPException,Depends
from passlib.context import CryptContext
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
from typing import Optional, List
from sqlalchemy.orm import Session
from . import models, schemas, utils
from . database import engine, SessionLocal, get_db
from . routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")
models.Base.metadata.create_all(bind=engine)

#try:
  #cnx = mysql.connector.connect(user='root', password = 'wyzecam53$DELMY', host = 'localhost',
                                #database= 'sakila')
  #cursor = cnx.cursor(dictionary = True)

 # print("successfully connected to the DATABASE!!")
#except mysql.connector.Error as err:
  #if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
   # print("Something is wrong with your user name or password")
  #elif err.errno == errorcode.ER_BAD_DB_ERROR:
    #print("Database does not exist")
  #else:
    #print(err)


my_posts = [{"title": "title of post1", "content": "content of post 1", "id": 1, "rating" : 4}, {"title": "favorite foods", "content": "I like pizza", 
"id":2}]


def find_post(id):
	for p in my_posts:
		if p["id"] == id: 
			return p
def find_index_post(id):
	for i, p in enumerate(my_posts):
		if p['id'] == id:
			return i

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {"message": "Frankley's API message!!!"}


@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
	posts = db.query(models.Post).all()
	return posts

@app.get("/posts/latest")
def get_latest_post():
	post = my_posts[len(my_posts)-1]
	return post