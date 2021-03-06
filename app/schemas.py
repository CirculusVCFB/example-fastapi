from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List
from pydantic.types import conint

class PostBase(BaseModel):
	title: str
	content: str
	published: bool = True

class PostCreate(PostBase):
	pass

class UserOut(BaseModel):
	id: int
	email: EmailStr
	created_at: datetime
	class Config:
		orm_mode = True

class Post(PostBase):
	id: int
	created_at: datetime
	user_id: int
	owner: UserOut
	class Config:
		orm_mode = True

class PostOut(BaseModel):
	Post: Post
	votes: int
	class Config:
		orm_mode = True


class UserCreate(BaseModel):
	email: EmailStr
	password: str

class UserLogin(BaseModel):
	email: EmailStr
	password: str

class Token(BaseModel):
	access_token: str
	token_type: str

class TokenData(BaseModel):
	id: Optional[str] = None

class Vote(BaseModel):
	post_id: int
	dir: conint(le = 1)

class Ticket(BaseModel):
	id: int
	amount: int
	lastupdated: datetime
	username: Optional[str] = None
	status: bool
	activated: bool
	class Config:
		orm_mode = True

class TicketCreate(BaseModel):
	amount: int
	status: bool = False
	activated: bool = False

class TicketUpdateUser(BaseModel):
	username: EmailStr
	status: bool
	started: bool
	completed: bool
	withdrawn: bool
	class Config:
		orm_mode = True

class TicketAmount(BaseModel):
	amount:int
