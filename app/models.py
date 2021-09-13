
# models.py
from sqlalchemy import Column, String, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN
import datetime
from uuid import uuid4
from enum import Enum

import hashlib

from database import Base


# User Model ORM
class User(Base):
    __tablename__ = "users"
    """
    User ORM Model
        id
        username
        password
        mail
    """
    id = Column(
        INTEGER, primary_key=True, index=True, default=uuid4
    )
    username = Column("username", String(256))
    password = Column("password", String(256))
    email = Column("mail", String(256))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    metrics = relationship("Metric", back_populates="owner")
    def __str__(self):
        return str(self.id) + ":" + self.username
    

# Tag ORM Model
class Tag(Base):
    """
    Tag ORM Model
    """
    __tablename__ = "tags"
    id = Column(
        INTEGER, primary_key=True, index=True, default=uuid4
    )
    display_name = Column("display_name", String(256))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )

    def __str__(self):
        return self.display_name
    
# MetricType ORM Model

class MetricType(Base):
    """MetricType
        id
        type_name
        created_at
        updated_at
    """
    __tablename__ = "metric_types"
    id = Column(
        INTEGER, primary_key=True, index=True, default=uuid4
    )
    type_name = Column("type_name", String(256))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )

    def __str__(self):
        return self.type_name

# Metric ORM Model

class Metric(Base):
    """
    Metric
        id
        created_at
        updated_at
        metric_value
        metric_type
        tag
        user

    """
    __tablename__ = "metrics"
    id = Column(
       INTEGER, primary_key=True, index=True, default=uuid4
    )
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    metric_value = Column("type_name", String(256))
    metric_type = relationship("MetricType")
    tag = relationship("Tag")
    owner = relationship("User", back_populates="users")
