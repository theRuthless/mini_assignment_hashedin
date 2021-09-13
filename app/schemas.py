# schemas.py 
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from models import Metric, MetricType, Tag
from typing import List, Optional
from datetime import datetime
from pydantic import UUID4, BaseModel
from pydantic.networks import EmailStr

# User Schema
class UserBase(BaseModel):
    email: Optional[EmailStr] = None


class UserCreate(UserBase):
    password: str



# Tag Schema
class TagBase(BaseModel):
    display_name: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int
    display_name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# MetricType Schema
class MetricTypeBase(BaseModel):
    type_name: str

class MetricTypeCreate(MetricTypeBase):
    pass

class MetricType(MetricTypeBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# Metric Schema
class MetricBase(BaseModel):
    metric_value: str

class MetricCreate(MetricBase):
    pass

class Metric(MetricBase):
    id: UUID4
    metric_value: str
    created_at: datetime
    updated_at: datetime
    owner_id: int

    class Config:
        orm_mode = True

# User Schema
class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    metrics: List[Metric] = []

    class Config:
        orm_mode = True
