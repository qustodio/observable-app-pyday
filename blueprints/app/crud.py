from datetime import datetime

from sqlalchemy.orm import Session
import models, schemas


def get_blueprint_by_id(db: Session, blueprint_id: int):
    return db.query(models.Blueprint).filter(models.Blueprint.id == blueprint_id).first()


def get_blueprints(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Blueprint).offset(skip).limit(limit).all()


def create_blueprint(db: Session, blueprint: schemas.BlueprintCreate):
    db_blueprint = models.Blueprint(
        **blueprint.dict(),
        created_at=datetime.now()
    )
    db.add(db_blueprint)
    db.commit()
    db.refresh(db_blueprint)
    return db_blueprint
