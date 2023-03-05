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


class Alembic(Base):
	__tablename__ = "alembic"
	id = Column(Integer, primary_key=True, nullable=False, index=True)
	title = Column(String(1000), nullable=False,)
	content = Column(String(1000), nullable=False)
	published = Column(Boolean, default = True)
	created_at = Column(TIMESTAMP(timezone = True ), nullable = False, server_default = text('now()'))
	user_id = Column(Integer, ForeignKey("users.id", ondelete = "CASCADE"), nullable = False)
	owner = relationship("User")

class Prizetablek1(Base):
	__tablename__ = "k1"
	id = Column(Integer, primary_key=True, index=True)
	amount = Column(Integer)
	lastupdated = Column(TIMESTAMP(timezone = True ), nullable = False, server_default = text('now()'))
	username = Column(String(1000))
	status = Column(Boolean)
	activated = Column(Boolean)
	started = Column(Boolean)
	completed = Column(Boolean)
	withdrawn = Column(Boolean)



class Prizetablek1(Base):
	__tablename__ = "k2"
	id = Column(Integer, primary_key=True, index=True)
	amount = Column(Integer)
	lastupdated = Column(TIMESTAMP(timezone = True ), nullable = False, server_default = text('now()'))
	username = Column(String(1000))
	status = Column(Boolean)
	activated = Column(Boolean)
	started = Column(Boolean)
	completed = Column(Boolean)
	withdrawn = Column(Boolean)


class Prizetablek1(Base):
	__tablename__ = "k3"
	id = Column(Integer, primary_key=True, index=True)
	amount = Column(Integer)
	lastupdated = Column(TIMESTAMP(timezone = True ), nullable = False, server_default = text('now()'))
	username = Column(String(1000))
	status = Column(Boolean)
	activated = Column(Boolean)
	started = Column(Boolean)
	completed = Column(Boolean)
	withdrawn = Column(Boolean)


class Prizetablek1(Base):
	__tablename__ = "k4"
	id = Column(Integer, primary_key=True, index=True)
	amount = Column(Integer)
	lastupdated = Column(TIMESTAMP(timezone = True ), nullable = False, server_default = text('now()'))
	username = Column(String(1000))
	status = Column(Boolean)
	activated = Column(Boolean)
	started = Column(Boolean)
	completed = Column(Boolean)
	withdrawn = Column(Boolean)



class Prizetablek10(Base):
	__tablename__ = "k10"
	id = Column(Integer, primary_key=True, index=True)
	amount = Column(Integer)
	lastupdated = Column(TIMESTAMP(timezone = True ), nullable = False, server_default = text('now()'))
	username = Column(String(1000))
	status = Column(Boolean)
	activated = Column(Boolean)
	started = Column(Boolean)
	completed = Column(Boolean)
	withdrawn = Column(Boolean)

class Prizetablek15(Base):
	__tablename__ = "k15"
	id = Column(Integer, primary_key=True, index=True)
	amount = Column(Integer)
	lastupdated = Column(TIMESTAMP(timezone = True ), nullable = False, server_default = text('now()'))
	username = Column(String(1000))
	status = Column(Boolean)
	activated = Column(Boolean)
	started = Column(Boolean)
	completed = Column(Boolean)
	withdrawn = Column(Boolean)

	
class Prizetablek20(Base):
	__tablename__ = "k20"
	id = Column(Integer, primary_key=True, index=True)
	amount = Column(Integer)
	lastupdated = Column(TIMESTAMP(timezone = True ), nullable = False, server_default = text('now()'))
	username = Column(String(1000))
	status = Column(Boolean)
	activated = Column(Boolean)
	started = Column(Boolean)
	completed = Column(Boolean)
	withdrawn = Column(Boolean)

class Prizetablek25(Base):
	__tablename__ = "k25"
	id = Column(Integer, primary_key=True, index=True)
	amount = Column(Integer)
	lastupdated = Column(TIMESTAMP(timezone = True ), nullable = False, server_default = text('now()'))
	username = Column(String(1000))
	status = Column(Boolean)
	activated = Column(Boolean)
	started = Column(Boolean)
	completed = Column(Boolean)
	withdrawn = Column(Boolean)


class Prizetablek50(Base):
	__tablename__ = "k50"
	id = Column(Integer, primary_key=True, index=True)
	amount = Column(Integer)
	lastupdated = Column(TIMESTAMP(timezone = True ), nullable = False, server_default = text('now()'))
	username = Column(String(1000))
	status = Column(Boolean)
	activated = Column(Boolean)
	started = Column(Boolean)
	completed = Column(Boolean)
	withdrawn = Column(Boolean)

class Prizetablek60(Base):
	__tablename__ = "k60"
	id = Column(Integer, primary_key=True, index=True)
	amount = Column(Integer)
	lastupdated = Column(TIMESTAMP(timezone = True ), nullable = False, server_default = text('now()'))
	username = Column(String(1000))
	status = Column(Boolean)
	activated = Column(Boolean)
	started = Column(Boolean)
	completed = Column(Boolean)
	withdrawn = Column(Boolean)

class Prizetablek70(Base):
	__tablename__ = "k70"
	id = Column(Integer, primary_key=True, index=True)
	amount = Column(Integer)
	lastupdated = Column(TIMESTAMP(timezone = True ), nullable = False, server_default = text('now()'))
	username = Column(String(1000))
	status = Column(Boolean)
	activated = Column(Boolean)
	started = Column(Boolean)
	completed = Column(Boolean)
	withdrawn = Column(Boolean)

class Prizetablek80(Base):
	__tablename__ = "k80"
	id = Column(Integer, primary_key=True, index=True)
	amount = Column(Integer)
	lastupdated = Column(TIMESTAMP(timezone = True ), nullable = False, server_default = text('now()'))
	username = Column(String(1000))
	status = Column(Boolean)
	activated = Column(Boolean)
	started = Column(Boolean)
	completed = Column(Boolean)
	withdrawn = Column(Boolean)

class Prizetablek100(Base):
	__tablename__ = "k100"
	id = Column(Integer, primary_key=True, index=True)
	amount = Column(Integer)
	lastupdated = Column(TIMESTAMP(timezone = True ), nullable = False, server_default = text('now()'))
	username = Column(String(1000))
	status = Column(Boolean)
	activated = Column(Boolean)
	started = Column(Boolean)
	completed = Column(Boolean)
	withdrawn = Column(Boolean)

class Prizetablek150(Base):
	__tablename__ = "k150"
	id = Column(Integer, primary_key=True, index=True)
	amount = Column(Integer)
	lastupdated = Column(TIMESTAMP(timezone = True ), nullable = False, server_default = text('now()'))
	username = Column(String(1000))
	status = Column(Boolean)
	activated = Column(Boolean)
	started = Column(Boolean)
	completed = Column(Boolean)
	withdrawn = Column(Boolean)

class Prizetablek200(Base):
	__tablename__ = "k200"
	id = Column(Integer, primary_key=True, index=True)
	amount = Column(Integer)
	lastupdated = Column(TIMESTAMP(timezone = True ), nullable = False, server_default = text('now()'))
	username = Column(String(1000))
	status = Column(Boolean)
	activated = Column(Boolean)
	started = Column(Boolean)
	completed = Column(Boolean)
	withdrawn = Column(Boolean)

class Prizetablek250(Base):
	__tablename__ = "k250"
	id = Column(Integer, primary_key=True, index=True)
	amount = Column(Integer)
	lastupdated = Column(TIMESTAMP(timezone = True ), nullable = False, server_default = text('now()'))
	username = Column(String(1000))
	status = Column(Boolean)
	activated = Column(Boolean)
	started = Column(Boolean)
	completed = Column(Boolean)
	withdrawn = Column(Boolean)

class Prizetablek300(Base):
	__tablename__ = "k300"
	id = Column(Integer, primary_key=True, index=True)
	amount = Column(Integer)
	lastupdated = Column(TIMESTAMP(timezone = True ), nullable = False, server_default = text('now()'))
	username = Column(String(1000))
	status = Column(Boolean)
	activated = Column(Boolean)
	started = Column(Boolean)
	completed = Column(Boolean)
	withdrawn = Column(Boolean)

class Prizetablek400(Base):
	__tablename__ = "k400"
	id = Column(Integer, primary_key=True, index=True)
	amount = Column(Integer)
	lastupdated = Column(TIMESTAMP(timezone = True ), nullable = False, server_default = text('now()'))
	username = Column(String(1000))
	status = Column(Boolean)
	activated = Column(Boolean)
	started = Column(Boolean)
	completed = Column(Boolean)
	withdrawn = Column(Boolean)

class Prizetablek500(Base):
	__tablename__ = "k500"
	id = Column(Integer, primary_key=True, index=True)
	amount = Column(Integer)
	lastupdated = Column(TIMESTAMP(timezone = True ), nullable = False, server_default = text('now()'))
	username = Column(String(1000))
	status = Column(Boolean)
	activated = Column(Boolean)
	started = Column(Boolean)
	completed = Column(Boolean)
	withdrawn = Column(Boolean)

class Prizetablek600(Base):
	__tablename__ = "k600"
	id = Column(Integer, primary_key=True, index=True)
	amount = Column(Integer)
	lastupdated = Column(TIMESTAMP(timezone = True ), nullable = False, server_default = text('now()'))
	username = Column(String(1000))
	status = Column(Boolean)
	activated = Column(Boolean)
	started = Column(Boolean)
	completed = Column(Boolean)
	withdrawn = Column(Boolean)