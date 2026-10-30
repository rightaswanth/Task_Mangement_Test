from datetime import datetime
from pydantic import BaseModel

class TaskCreate(BaseModel):
    name: str
    priority: int
    description: str
    due_date: datetime = None

class TaskResponse(BaseModel):
    id: int
    name: str
    description: str
    priority: int
    due_date: datetime = None