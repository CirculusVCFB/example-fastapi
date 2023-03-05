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




# The 1s Start here



@router.put("/tickets/change/prizetablek1")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek1).filter(models.Prizetablek1.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek1).filter(models.Prizetablek1.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()




@router.put("/tickets/complete/prizetablek1")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket, current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek1).filter(models.Prizetablek1.username == ticket.username, models.Prizetablek1.started == True, models.Prizetablek1.completed == False).first()
	ticket_to_grab = db.query(models.Prizetablek1).filter(models.Prizetablek1.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	return ticket_to_grab.first()


# The 2s Start here

@router.put("/tickets/change/prizetablek2")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek2).filter(models.Prizetablek2.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek2).filter(models.Prizetablek2.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()




@router.put("/tickets/complete/prizetablek2")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket, current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek2).filter(models.Prizetablek2.username == ticket.username, models.Prizetablek2.started == True, models.Prizetablek2.completed == False).first()
	ticket_to_grab = db.query(models.Prizetablek2).filter(models.Prizetablek2.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	return ticket_to_grab.first()

# The 3s Start here


@router.put("/tickets/change/prizetablek3")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek3).filter(models.Prizetablek3.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek3).filter(models.Prizetablek3.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()




@router.put("/tickets/complete/prizetablek3")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket, current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek3).filter(models.Prizetablek3.username == ticket.username, models.Prizetablek3.started == True, models.Prizetablek3.completed == False).first()
	ticket_to_grab = db.query(models.Prizetablek3).filter(models.Prizetablek3.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	return ticket_to_grab.first()


# The 4s Start here


@router.put("/tickets/change/prizetablek4")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek4).filter(models.Prizetablek4.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek4).filter(models.Prizetablek4.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()




@router.put("/tickets/complete/prizetablek4")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket, current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek4).filter(models.Prizetablek4.username == ticket.username, models.Prizetablek4.started == True, models.Prizetablek4.completed == False).first()
	ticket_to_grab = db.query(models.Prizetablek4).filter(models.Prizetablek4.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	return ticket_to_grab.first()




# The 10s Start here



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
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket, current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek10).filter(models.Prizetablek10.username == ticket.username, models.Prizetablek10.started == True, models.Prizetablek10.completed == False).first()
	ticket_to_grab = db.query(models.Prizetablek10).filter(models.Prizetablek10.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	return ticket_to_grab.first()
	




@router.put("/tickets/change/prizetablek15")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek15).filter(models.Prizetablek15.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek15).filter(models.Prizetablek15.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()


@router.put("/tickets/complete/prizetablek15")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket, current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek15).filter(models.Prizetablek15.username == ticket.username, models.Prizetablek15.started == True, models.Prizetablek15.completed == False).first()
	ticket_to_grab = db.query(models.Prizetablek15).filter(models.Prizetablek15.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	return ticket_to_grab.first()


# The 20s start here


@router.put("/tickets/change/prizetablek20")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek20).filter(models.Prizetablek20.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek20).filter(models.Prizetablek20.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()


@router.put("/tickets/complete/prizetablek20")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket, current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek20).filter(models.Prizetablek20.username == ticket.username, models.Prizetablek20.started == True, models.Prizetablek20.completed == False).first()
	ticket_to_grab = db.query(models.Prizetablek20).filter(models.Prizetablek20.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	return ticket_to_grab.first()


# The 25s start here	


@router.put("/tickets/change/prizetablek25")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek25).filter(models.Prizetablek25.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek25).filter(models.Prizetablek25.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()


@router.put("/tickets/complete/prizetablek25")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket, current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek25).filter(models.Prizetablek25.username == ticket.username, models.Prizetablek25.started == True, models.Prizetablek20.completed == False).first()
	ticket_to_grab = db.query(models.Prizetablek25).filter(models.Prizetablek25.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	return ticket_to_grab.first()



# The 50s start here



@router.put("/tickets/change/prizetablek50")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek50).filter(models.Prizetablek50.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek50).filter(models.Prizetablek50.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()


@router.put("/tickets/complete/prizetablek50")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket, current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek50).filter(models.Prizetablek50.username == ticket.username, models.Prizetablek50.started == True, models.Prizetablek50.completed == False).first()
	ticket_to_grab = db.query(models.Prizetablek50).filter(models.Prizetablek50.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	return ticket_to_grab.first()



# The 60s start here



@router.put("/tickets/change/prizetablek60")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek60).filter(models.Prizetablek60.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek60).filter(models.Prizetablek60.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()



@router.put("/tickets/complete/prizetablek60")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket, current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek60).filter(models.Prizetablek60.username == ticket.username, models.Prizetablek60.started == True, models.Prizetablek60.completed == False).first()
	ticket_to_grab = db.query(models.Prizetablek60).filter(models.Prizetablek60.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	return ticket_to_grab.first()



# The 70s start here


@router.put("/tickets/complete/prizetablek70")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket, current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek70).filter(models.Prizetablek70.username == ticket.username, models.Prizetablek70.started == True, models.Prizetablek70.completed == False).first()
	ticket_to_grab = db.query(models.Prizetablek70).filter(models.Prizetablek70.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
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


# The 80s start here


@router.put("/tickets/change/prizetablek80")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek80).filter(models.Prizetablek80.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek80).filter(models.Prizetablek80.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()


@router.put("/tickets/complete/prizetablek80")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket, current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek80).filter(models.Prizetablek80.username == ticket.username, models.Prizetablek80.started == True, models.Prizetablek80.completed == False).first()
	ticket_to_grab = db.query(models.Prizetablek80).filter(models.Prizetablek80.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	return ticket_to_grab.first()



# The 100s start here



@router.put("/tickets/change/prizetablek100")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek100).filter(models.Prizetablek100.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek100).filter(models.Prizetablek100.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()


@router.put("/tickets/complete/prizetablek100")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket, current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek100).filter(models.Prizetablek100.username == ticket.username, models.Prizetablek100.started == True, models.Prizetablek80.completed == False).first()
	ticket_to_grab = db.query(models.Prizetablek100).filter(models.Prizetablek100.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	return ticket_to_grab.first()



# The 150s start here



@router.put("/tickets/change/prizetablek150")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek150).filter(models.Prizetablek150.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek150).filter(models.Prizetablek150.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()


@router.put("/tickets/complete/prizetablek150")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket, current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek150).filter(models.Prizetablek150.username == ticket.username, models.Prizetablek150.started == True, models.Prizetablek150.completed == False).first()
	ticket_to_grab = db.query(models.Prizetablek150).filter(models.Prizetablek150.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	return ticket_to_grab.first()



# The 200s start here


@router.put("/tickets/change/prizetablek200")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek200).filter(models.Prizetablek200.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek200).filter(models.Prizetablek200.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()




@router.put("/tickets/complete/prizetablek200")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket, current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek200).filter(models.Prizetablek200.username == ticket.username, models.Prizetablek200.started == True, models.Prizetablek200.completed == False).first()
	ticket_to_grab = db.query(models.Prizetablek200).filter(models.Prizetablek200.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	return ticket_to_grab.first()


# The 250s start here


@router.put("/tickets/change/prizetablek250")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek250).filter(models.Prizetablek250.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek250).filter(models.Prizetablek250.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()

@router.put("/tickets/complete/prizetablek250")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket, current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek250).filter(models.Prizetablek80.username == ticket.username, models.Prizetablek250.started == True, models.Prizetablek250.completed == False).first()
	ticket_to_grab = db.query(models.Prizetablek250).filter(models.Prizetablek250.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	return ticket_to_grab.first()


# The 300s start here

@router.put("/tickets/change/prizetablek300")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek300).filter(models.Prizetablek300.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek300).filter(models.Prizetablek300.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()

@router.put("/tickets/complete/prizetablek300")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket, current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek300).filter(models.Prizetablek300.username == ticket.username, models.Prizetablek300.started == True, models.Prizetablek300.completed == False).first()
	ticket_to_grab = db.query(models.Prizetablek300).filter(models.Prizetablek300.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	return ticket_to_grab.first()

# The 400s start here



@router.put("/tickets/change/prizetablek400")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek400).filter(models.Prizetablek400.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek400).filter(models.Prizetablek400.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()




@router.put("/tickets/complete/prizetablek400")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket, current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek400).filter(models.Prizetablek400.username == ticket.username, models.Prizetablek400.started == True, models.Prizetablek400.completed == False).first()
	ticket_to_grab = db.query(models.Prizetablek400).filter(models.Prizetablek400.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	return ticket_to_grab.first()



# The 500s start here



@router.put("/tickets/change/prizetablek500")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek500).filter(models.Prizetablek500.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek500).filter(models.Prizetablek500.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()




@router.put("/tickets/complete/prizetablek500")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket, current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek500).filter(models.Prizetablek500.username == ticket.username, models.Prizetablek500.started == True, models.Prizetablek500.completed == False).first()
	ticket_to_grab = db.query(models.Prizetablek500).filter(models.Prizetablek500.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	return ticket_to_grab.first()


# The 600s start here


@router.put("/tickets/change/prizetablek600")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket,
	current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek600).filter(models.Prizetablek600.username == None).first()
	ticket_to_grab = db.query(models.Prizetablek600).filter(models.Prizetablek600.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
	print(tickets)
	return ticket_to_grab.first()



@router.put("/tickets/complete/prizetablek600")
def update_ticket(ticket: schemas.TicketUpdateUser, db: Session = Depends(get_db), response_model=schemas.Ticket, current_user: int = Depends(oauth2.get_current_user)):
	tickets = db.query(models.Prizetablek600).filter(models.Prizetablek600.username == ticket.username, models.Prizetablek600.started == True, models.Prizetablek600.completed == False).first()
	ticket_to_grab = db.query(models.Prizetablek600).filter(models.Prizetablek600.id == tickets.id )
	ticket_to_grab.update(ticket.dict(), synchronize_session = False)
	db.commit()
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