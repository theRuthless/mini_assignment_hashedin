from typing import Optional
from sqlalchemy.orm import Session
from . import models, schemas


def get_user(db: Session, user_id: int):
    """GET User
        user_id: int
    """

    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    """GET User by email
        email: str
    """

    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """GET List of Users
        skip: optional
        limit: optional
    """

    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    """POST User
        user: UserCreate
    """
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_metrics(db: Session, skip: int = 0, limit: int = 100):
    """GET metrics
        skip: optional
        limit: optional
    """
    return db.query(models.Metric).offset(skip).limit(limit).all()

def create_user_metric(db: Session, metric: schemas.MetricCreate):
    db_metric = models.Metric(**metric.dict())
    db.add(db_metric)
    db.commit()
    db.refresh(db_metric)
    return db_metric

def get_tags(db: Session, skip: int = 0, limit: int = 100):
    """GET List of Tags
        skip: optional
        limit: optional
    """
    
    return db.query(models.Tag).offset(skip).limit(limit).all()

def get_tag(db: Session, tag_id: int):
    """GET Tag
        tag_id: int
    """

    return db.query(models.Tag).filter(models.Tag.id == tag_id).first()

def get_tag_by_display_name(db: Session, display_name: str) -> Optional[models.Tag]:
    return db.query(models.Tag).filter(models.Tag.display_name==display_name).first()

def add_tag(
        db: Session,
        tag: schemas.TagCreate,
) -> Optional[models.Tag]:
    tag: models.Tag = models.Tag(
        **tag.dict()
    )
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag

def delete_tag(
        db: Session,
        tag_id: int,
):
    tag: models.Tag = db.query(models.Tag).filter(models.Tag.id == tag_id).first()
    db.delete(tag)
    db.commit()

def get_metric_type(db: Session, metric_type_id: int):
    """GET Metric Type
        metric_type_id: int
    """

    return db.query(models.MetricType).filter(models.MetricType.id == metric_type_id).first()

def get_metric_types(db: Session, skip: int = 0, limit: int = 100):
    """GET List of Metric types
        skip: optional
        limit: optional
    """
    
    return db.query(models.MetricType).offset(skip).limit(limit).all()

def get_metric_type_by_type_name(db: Session, type_name: str) -> Optional[models.MetricType]:
    return db.query(models.MetricType).filter(models.MetricType.type_name==type_name).first()


def add_metric_type(
        db: Session,
        metric_type: schemas.MetricCreate,
) -> Optional[models.MetricType]:
    metric_type: models.MetricType = models.MetricType(
        **metric_type.dict()
    )
    db.add(metric_type)
    db.commit()
    db.refresh(metric_type)
    return metric_type

def delete_metric_type(
        db: Session,
        metric_id: int,
):
    metric_type: models.MetricType = db.query(models.MetricType).filter(models.MetricType.id == metric_id).first()
    db.delete(metric_type)
    db.commit()

