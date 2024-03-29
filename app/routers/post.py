import time
from fastapi import FastAPI, Response,status,HTTPException,Depends, APIRouter
from passlib.context import CryptContext
from fastapi.params import Body
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from .. import models, schemas, utils, oauth2
from .. database import engine, SessionLocal, get_db


router = APIRouter(
	prefix = "/posts",
	tags = ["Posts"]
	)


#@router.get("/", response_model=List[schemas.Post])
#@router.get("/", response_model=List[schemas.PostOut])
#async def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),limit:int = 10,
	#skip: int = 0, search:Optional[str] = "" ):
	#Left SQL for future reference
	#cursor.execute("SELECT * FROM posts")
	#posts = cursor.fetchall()
	# print(limit)
	#posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

	#posts = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id,
		#isouter = True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
	#return posts

@router.post("/", status_code = status.HTTP_201_CREATED, response_model=schemas.Post)
async def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), 
	current_user: int = Depends(oauth2.get_current_user)) :
	#cursor.execute("INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) ", (post.title, post.content, post.published))
	#cnx.commit()
 	#new_post = models.Post(title=post.title, content= post.content, published= post.published)
 	print(current_user.id)
 	print(current_user.email)
 	new_post = models.Post(user_id = current_user.id, **post.dict())
 	db.add(new_post)
 	db.commit()
 	db.refresh(new_post)
 	return new_post

@router.get("/{id}", response_model=schemas.PostOut)
# Converting to int for validation purposes 
async def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
	#cursor.execute("SELECT * FROM posts WHERE id = %s", (str(id),))
	#post = cursor.fetchone()
	#post = db.query(models.Post).filter(models.Post.id == id).first()

	post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id,
		isouter = True).group_by(models.Post.id).filter(models.Post.id == id).first()
	if not post:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"post with id: {id} was not found")
	return post


@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
async def delete_post(id: int, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
	#cursor.execute("DELETE FROM posts WHERE id = %s", (str(id),))
	#cnx.commit()
	# Tutorial uese return Response(status_code = status.HTTP_204_NO_CONTENT)
	# However, my solution works a message is returned whereas in the tutorial an error was raised
	
	post_query=db.query(models.Post).filter(models.Post.id == id)

	post = post_query.first()
	
	if post== None:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"post with id: {id} does not exist")

	if post.user_id !=current_user.id:
		raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = "Not authorized to pearform requested action")

	post_query.delete(synchronize_session = False)
	db.commit()



	return {"message": "post was successfully deleted"}

@router.put("/{id}", response_model=schemas.Post)
async def update_post(id:int , updated_post: schemas.PostCreate, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
	#cursor.execute("UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s ", (post.title, post.content, post.published, str(id)))
	#cnx.commit()                                                                                                        
	post_query = db.query(models.Post).filter(models.Post.id == id)

	post = post_query.first()

	if post == None:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"post with id: {id} was not found")

	if post.user_id != current_user.id:
		raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = "Not authorized to pearform requested action")

	post_query.update(updated_post.dict(), synchronize_session = False)

	db.commit()

	return post_query.first()
