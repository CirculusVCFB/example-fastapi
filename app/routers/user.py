import time
from fastapi import FastAPI, Response,status,HTTPException,Depends, APIRouter, Form
from passlib.context import CryptContext
from fastapi.params import Body
from sqlalchemy.orm import Session
from sqlalchemy.sql import func, update
from sqlalchemy import update
from typing import List
from .. import models, schemas, utils, oauth2
from .. database import engine, SessionLocal, get_db
from enum import Enum

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
def get_ticket(db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek10).filter(models.Prizetablek10.username == None).first()
	return tickets

@router.put("/tickets/change/prizetablek10")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek10).filter(models.Prizetablek10.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek10).filter(models.Prizetablek10.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()

@router.put("/tickets/complete/prizetablek10")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek10).filter(models.Prizetablek10.username == ticket.username)
	print("The tickets are")
	print(tickets)




@router.put("/tickets/change/prizetablek15")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek15).filter(models.Prizetablek15.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek15).filter(models.Prizetablek15.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()

@router.put("/tickets/change/prizetablek20")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek20).filter(models.Prizetablek20.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek20).filter(models.Prizetablek20.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()

@router.put("/tickets/change/prizetablek25")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek25).filter(models.Prizetablek25.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek25).filter(models.Prizetablek25.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()

@router.put("/tickets/change/prizetablek50")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek50).filter(models.Prizetablek50.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek50).filter(models.Prizetablek50.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()

@router.put("/tickets/change/prizetablek60")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek60).filter(models.Prizetablek60.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek60).filter(models.Prizetablek60.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()


@router.put("/tickets/change/prizetablek70")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek70).filter(models.Prizetablek70.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek70).filter(models.Prizetablek70.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()

@router.put("/tickets/change/prizetablek80")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek80).filter(models.Prizetablek80.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek80).filter(models.Prizetablek80.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()

@router.put("/tickets/change/prizetablek100")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek100).filter(models.Prizetablek100.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek100).filter(models.Prizetablek100.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()

@router.put("/tickets/change/prizetablek150")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek150).filter(models.Prizetablek150.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek150).filter(models.Prizetablek150.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()

@router.put("/tickets/change/prizetablek200")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek200).filter(models.Prizetablek200.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek200).filter(models.Prizetablek200.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()

@router.put("/tickets/change/prizetablek250")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek250).filter(models.Prizetablek250.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek250).filter(models.Prizetablek250.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()

@router.put("/tickets/change/prizetablek300")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek300).filter(models.Prizetablek300.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek300).filter(models.Prizetablek300.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()

@router.put("/tickets/change/prizetablek400")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek400).filter(models.Prizetablek400.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek400).filter(models.Prizetablek400.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()

@router.put("/tickets/change/prizetablek500")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek500).filter(models.Prizetablek500.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek500).filter(models.Prizetablek500.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()

@router.put("/tickets/change/prizetablek600")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek600).filter(models.Prizetablek600.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek600).filter(models.Prizetablek600.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()


@router.post("/tickets/add", status_code = status.HTTP_201_CREATED,response_model=schemas.Ticket)
def post_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db),
	current_user: int = Depends(oauth2.get_current_user)):
	new_ticket = models.Prizetablek10(**ticket.dict())
	db.add(new_ticket)
	db.commit()
	db.refresh(new_ticket)
	return new_ticket

@router.post("/tickets/add/Prizetablek15", status_code = status.HTTP_201_CREATED,response_model=schemas.Ticket)
def post_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db),
	current_user: int = Depends(oauth2.get_current_user)):
	new_ticket = models.Prizetablek15(**ticket.dict())
	db.add(new_ticket)
	db.commit()
	db.refresh(new_ticket)
	return new_ticket
	
@router.post("/tickets/add/Prizetablek20", status_code = status.HTTP_201_CREATED,response_model=schemas.Ticket)
def post_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db),
	current_user: int = Depends(oauth2.get_current_user)):
	new_ticket = models.Prizetablek20(**ticket.dict())
	db.add(new_ticket)
	db.commit()
	db.refresh(new_ticket)
	return new_ticket

@router.post("/tickets/add/Prizetablek25", status_code = status.HTTP_201_CREATED,response_model=schemas.Ticket)
def post_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db),
	current_user: int = Depends(oauth2.get_current_user)):
	new_ticket = models.Prizetablek25(**ticket.dict())
	db.add(new_ticket)
	db.commit()
	db.refresh(new_ticket)
	return new_ticket


@router.post("/tickets/add/Prizetablek50", status_code = status.HTTP_201_CREATED,response_model=schemas.Ticket)
def post_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db),
	current_user: int = Depends(oauth2.get_current_user)):
	new_ticket = models.Prizetablek50(**ticket.dict())
	db.add(new_ticket)
	db.commit()
	db.refresh(new_ticket)
	return new_ticket
	

@router.post("/tickets/add/Prizetablek60", status_code = status.HTTP_201_CREATED,response_model=schemas.Ticket)
def post_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db),
	current_user: int = Depends(oauth2.get_current_user)):
	new_ticket = models.Prizetablek60(**ticket.dict())
	db.add(new_ticket)
	db.commit()
	db.refresh(new_ticket)
	return new_ticket


@router.post("/tickets/add/Prizetablek70", status_code = status.HTTP_201_CREATED,response_model=schemas.Ticket)
def post_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db),
	current_user: int = Depends(oauth2.get_current_user)):
	new_ticket = models.Prizetablek70(**ticket.dict())
	db.add(new_ticket)
	db.commit()
	db.refresh(new_ticket)
	return new_ticket

@router.post("/tickets/add/Prizetablek80", status_code = status.HTTP_201_CREATED,response_model=schemas.Ticket)
def post_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db),
	current_user: int = Depends(oauth2.get_current_user)):
	new_ticket = models.Prizetablek80(**ticket.dict())
	db.add(new_ticket)
	db.commit()
	db.refresh(new_ticket)
	return new_ticket

@router.post("/tickets/add/Prizetablek100", status_code = status.HTTP_201_CREATED,response_model=schemas.Ticket)
def post_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db),
	current_user: int = Depends(oauth2.get_current_user)):
	new_ticket = models.Prizetablek100(**ticket.dict())
	db.add(new_ticket)
	db.commit()
	db.refresh(new_ticket)
	return new_ticket

@router.post("/tickets/add/Prizetablek150", status_code = status.HTTP_201_CREATED,response_model=schemas.Ticket)
def post_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db),
	current_user: int = Depends(oauth2.get_current_user)):
	new_ticket = models.Prizetablek150(**ticket.dict())
	db.add(new_ticket)
	db.commit()
	db.refresh(new_ticket)
	return new_ticket

@router.post("/tickets/add/Prizetablek200", status_code = status.HTTP_201_CREATED,response_model=schemas.Ticket)
def post_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db),
	current_user: int = Depends(oauth2.get_current_user)):
	new_ticket = models.Prizetablek200(**ticket.dict())
	db.add(new_ticket)
	db.commit()
	db.refresh(new_ticket)
	return new_ticket

@router.post("/tickets/add/Prizetablek250", status_code = status.HTTP_201_CREATED,response_model=schemas.Ticket)
def post_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db),
	current_user: int = Depends(oauth2.get_current_user)):
	new_ticket = models.Prizetablek250(**ticket.dict())
	db.add(new_ticket)
	db.commit()
	db.refresh(new_ticket)
	return new_ticket


@router.post("/tickets/add/Prizetablek300", status_code = status.HTTP_201_CREATED,response_model=schemas.Ticket)
def post_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db),
	current_user: int = Depends(oauth2.get_current_user)):
	new_ticket = models.Prizetablek300(**ticket.dict())
	db.add(new_ticket)
	db.commit()
	db.refresh(new_ticket)
	return new_ticket


@router.post("/tickets/add/Prizetablek400", status_code = status.HTTP_201_CREATED,response_model=schemas.Ticket)
def post_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db),
	current_user: int = Depends(oauth2.get_current_user)):
	new_ticket = models.Prizetablek400(**ticket.dict())
	db.add(new_ticket)
	db.commit()
	db.refresh(new_ticket)
	return new_ticket


@router.post("/tickets/add/Prizetablek500", status_code = status.HTTP_201_CREATED,response_model=schemas.Ticket)
def post_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db),
	current_user: int = Depends(oauth2.get_current_user)):
	new_ticket = models.Prizetablek500(**ticket.dict())
	db.add(new_ticket)
	db.commit()
	db.refresh(new_ticket)
	return new_ticket

@router.post("/tickets/add/Prizetablek600", status_code = status.HTTP_201_CREATED,response_model=schemas.Ticket)
def post_ticket(ticket: schemas.TicketCreate, db: Session = Depends(get_db),
	current_user: int = Depends(oauth2.get_current_user)):
	new_ticket = models.Prizetablek600(**ticket.dict())
	db.add(new_ticket)
	db.commit()
	db.refresh(new_ticket)
	return new_ticket