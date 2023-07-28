
from pydantic import BaseModel, Field, validator
from typing import Optional
import re
from sqlalchemy import Column, Integer, String, Float, Boolean
from database.db import Base

class UserModel(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

    def __str__(self):
        return f"User {self.username}, id {self.id}"

class User(BaseModel):
	id : int
	username : str = Field(..., max_length=20, min_length=3)
	email : str
	password : str 

	@validator('password')
	def check_password(cls, password):
		if len(password) < 8:
			raise("Password less than 8")
		return password

	@validator('email')
	def check_email(cls, email):
		regex = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
		if re.fullmatch(regex, email):
			return email
		else:
			raise("Email is not valid")