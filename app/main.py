import logging
from typing import List, Optional
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from pydantic.errors import PydanticValueError
from pydantic.utils import import_string
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from app.utils import get_logger

logger = get_logger(__name__)


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Data Metric(s) collector", description="collects data for various matrics related to user")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# Dependency
def get_db(request: Request):
    return request.state.db

@app.get("/health")
def health():
    logger.info({"message": "ok!"})
    return {"message": "ok!"}

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)) -> Optional[models.User]:
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> Optional[List[models.User]]:
    
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)) -> Optional[models.User]:
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users/metrics/", response_model=schemas.MetricCreate)
def create_metric_for_user(
   metric: schemas.MetricCreate, db: Session = Depends(get_db)
) -> Optional[models.Metric]:
    return crud.create_user_metric(db=db, metric=metric)

@app.get("/metrics/", response_model=List[schemas.Metric])
def read_metrices(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> Optional[List[models.Metric]]:
    metrics = crud.get_metrics(db, skip=skip, limit=limit)
    return metrics

@app.get("/tags/", response_model=List[schemas.Tag])
def get_tags(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> Optional[List[models.Tag]]:
    tags = crud.get_tags(db, skip=skip, limit=limit)
    return tags

@app.get("/tags/{tag_id}", response_model=schemas.Tag)
def get_tag(tag_id: int,db: Session = Depends(get_db)) -> Optional[models.Tag]:
    db_tag = crud.get_tag(db, tag_id=tag_id)
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag

@app.post("/tags/", response_model=schemas.Tag)
def create_tag(tag: schemas.TagCreate, db: Session = Depends(get_db)) -> Optional[models.Tag]:
    db_tag = crud.get_tag_by_display_name(db, display_name=tag.display_name)
    if db_tag:
        raise HTTPException(status_code=400, detail="Tag already registered")
    return crud.add_tag(db=db, tag=tag)

@app.get("/metric_types/", response_model=List[schemas.MetricType])
def get_metric_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> Optional[List[models.MetricType]]:
    metric_types = crud.get_metric_types(db, skip=skip, limit=limit)
    return metric_types

@app.get("/metric_types/{metric_type_id}", response_model=schemas.MetricType)
def get_metric_types(metric_type_id: int,db: Session = Depends(get_db)) -> Optional[models.MetricType]:
    metric_type = crud.get_metric_type(db, metric_type_id=metric_type_id)
    if metric_type is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return metric_type

@app.post("/metric_types/", response_model=schemas.MetricType)
def create_metric_type(metric: schemas.MetricTypeCreate, db: Session = Depends(get_db)) -> Optional[models.MetricType]:
    db_metric_type = crud.get_metric_type_by_type_name(db, type_name=metric.type_name)
    if db_metric_type:
        raise HTTPException(status_code=400, detail="Metric Type already registered")
    return crud.add_metric_type(db=db, metric_type=metric)
