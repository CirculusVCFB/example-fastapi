import time
from fastapi import FastAPI, Response,status,HTTPException,Depends, APIRouter, Form
from passlib.context import CryptContext
from fastapi.params import Body
from sqlalchemy.orm import Session, update
from typing import List
from .. import models, schemas, utils
from .. database import engine, SessionLocal, get_db

router = APIRouter(
	prefix = "/users",
	tags = ["Users"]
	)


@router.post("/", status_code = status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
	hashed_password = utils.hash(user.password)
	user.password = hashed_password
	new_user = models.User(**user.dict())
	user_info = db.query(models.User).filter(models.User.email == new_user.email).first()
	if user_info == None:
		db.add(new_user)
		db.commit()
		db.refresh(new_user)

	if user_info != None:
		raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = "Not authorized to pearform requested action")
	return new_user


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
	user = db.query(models.User).filter(models.User.id == id).first()
	if not user:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"User with id: {id} does not exist")

	return user

@router.get("/tickets/grab")
def get_ticket(db: Session = Depends(get_db)):
	tickets = db.query(models.Prizetablek10).filter(models.Prizetablek10.username == None).first()
	return tickets

@router.post("/tickets/add", status_code = status.HTTP_201_CREATED, response_model=schemas.Ticket)
def post_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db)):
	new_ticket = models.Prizetablek10(**ticket.dict())
	db.add(new_ticket)
	db.commit()
	db.refresh(new_ticket)

	return new_ticket

@router.put("/tickets/change")
def update_ticket(ticket:schemas.TicketUpdateUser, db: Session = Depends(get_db)):
	tickets = db.query(models.Prizetablek10).filter(models.Prizetablek10.username == None).first()
	amount = tickets.amount
	tickets.update(ticket.dict(), synchronize_session = False)
	db.commit()
	return tickets








