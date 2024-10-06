import uuid
from sqlalchemy import Column, String, Text, Integer, ForeignKey, TIMESTAMP, UUID
from datetime import datetime, timedelta

from .base import Model

class Session(Model):
    __tablename__ = 'sessions'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_name = Column(Text, nullable=True)
    proxy_text = Column(Text, nullable=True)
    