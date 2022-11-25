import logging
import sys

import httpx
import uvicorn
from fastapi import FastAPI, Response, Request, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

logger = logging.getLogger("uvicorn.blueprints")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user(request: Request):
    header_token = request.headers.get("Authorization")
    if header_token is not None:
        response = httpx.get(
            url='http://users:8000/users/me',
            headers={
                "Authorization": header_token
            }
        )

        return response.json()


@app.get("/blueprints", response_model=list[schemas.Blueprint])
def read_blueprints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    bps = crud.get_blueprints(db, skip=skip, limit=limit)
    return bps


@app.post("/blueprint", response_model=schemas.Blueprint)
def create_blueprint(bp: schemas.BlueprintCreate, request: Request, db: Session = Depends(get_db)):
    user = get_user(request)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized user"
        )
    logger.info(f"Created blueprint by: {user['username']}")
    bp = crud.create_blueprint(db=db, blueprint=bp)
    return bp


@app.get("/blueprint/{bp_id}", response_model=schemas.Blueprint)
def read_blueprint_by_id(bp_id: int, db: Session = Depends(get_db)):
    db_blueprint = crud.get_blueprint_by_id(db, blueprint_id=bp_id)
    if db_blueprint is None:
        raise HTTPException(
            status_code=404,
            detail="Blueprint not found"
        )
    return db_blueprint


@app.on_event("startup")
async def startup_event():
    logger = logging.getLogger("uvicorn")
    formatter = logging.Formatter("[%(asctime)s] - %(name)s - %(levelname)s - %(message)s")
    for handler in logger.handlers:
        handler.setFormatter(formatter)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
