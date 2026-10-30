from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class Tasks(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    priority = Column(Integer, index=True)
    due_date = Column(DateTime(timezone=True))
