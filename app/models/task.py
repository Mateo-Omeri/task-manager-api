from pydantic import BaseModel, Field
from typing import Optional
from uuid import uuid4
from sqlalchemy import Column, Integer, String, Boolean
from app.db import Base

class Task(Base):
    
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    
