from sqlalchemy import Column, Integer, String, TIMESTAMP
from datetime import datetime, timedelta

from .base import Model

class Sessions(Model):
    __tablename__ = 'sessions'

    session_name = Column(Integer, primary_key=True, unique=True)
    