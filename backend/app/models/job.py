from sqlalchemy import Column, String, JSON
from app.core.base import Base


class Job(Base):

    __tablename__ = "jobs"

    id = Column(String, primary_key=True)

    status = Column(String)

    result = Column(JSON, nullable=True)