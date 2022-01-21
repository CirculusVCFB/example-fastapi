from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class Post(Base):
	__tablename__ = "posts"
	id = Column(Integer, primary_key=True, nullable=False, index=True)
	title = Column(String(1000), nullable=False,)
	content = Column(String(1000), nullable=False)
	published = Column(Boolean, default = True)
	created_at = Column(TIMESTAMP(timezone = True ), nullable = False, server_default = text('now()'))
	user_id = Column(Integer, ForeignKey("users.id", ondelete = "CASCADE"), nullable = False)
	owner = relationship("User")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100))
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP(timezone = True ), nullable = False, server_default = text('now()'))


class Vote(Base):
	__tablename__ = "votes"

	user_id = Column(Integer, ForeignKey("users.id", ondelete = "CASCADE"), primary_key = True)
	post_id = Column(Integer, ForeignKey("posts.id", ondelete = "CASCADE"), primary_key = True)


#class Alembic(Base):
	#__tablename__ = "alembic"
	#id = Column(Integer, primary_key=True, nullable=False, index=True)
	#title = Column(String(1000), nullable=False,)
	#content = Column(String(1000), nullable=False)
	#published = Column(Boolean, default = True)
	#created_at = Column(TIMESTAMP(timezone = True ), nullable = False, server_default = text('now()'))
	#user_id = Column(Integer, ForeignKey("users.id", ondelete = "CASCADE"), nullable = False)
	#owner = relationship("User")
