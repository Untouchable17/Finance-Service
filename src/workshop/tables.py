import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, unique=True)
    email = db.Column(db.Text, unique=True)
    password_hash = db.Column(db.Text)


class Operation(Base):
    __tablename__ = "operations"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    date = db.Column(db.Date)
    kind = db.Column(db.String)
    amount = db.Column(db.Numeric(10, 2))
    description = db.Column(db.String, nullable=True)
