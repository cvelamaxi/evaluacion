
from fastapi import FastAPI, Depends, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session

from model.user import User, UserModel
from database.db import get_db

app = FastAPI()

@app.get("/")
async def getInit():
	return "Perfecto v1.0"

@app.post("/users")
async def createUser(user : User, db: Session = Depends(get_db)):
	try:
		db_user = UserModel(id = user.id, username = user.username, email = user.email, password = user.password )
		db.add(db_user)
		db.commit()
		db.refresh(db_user)
		print(db_user)
		return db_user
	except:
		return JSONResponse(status_code=status.HTTP_409_CONFLICT , content={"error": "Ocurrio un error al insertar el usuario"})

@app.get("/users/{id_user}")
async def getUser( id_user : int = 0, db: Session = Depends(get_db)):
	item = db.query(UserModel).filter(UserModel.id == id_user).first()
	if item:
		return item
	return JSONResponse(status_code = status.HTTP_404_NOT_FOUND, content={"error": "item not found"})