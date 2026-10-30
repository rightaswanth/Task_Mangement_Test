from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import Base, engine, get_db
from schema import TaskCreate, TaskResponse
from models import Tasks


app = FastAPI()


@app.on_event("startup")
async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.post("/tasks/", response_model=TaskResponse)
async def create_item(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    db_item = Tasks(**task.model_dump())
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item


@app.get("/tasks/{task_id}", response_model=TaskResponse)
async def list_task(task_id: int, db: AsyncSession = Depends(get_db)):
    stmt = select(Tasks).where(Tasks.id == task_id)
    result = await db.execute(stmt)
    db_item = result.scalar_one_or_none()

    if not db_item:
        raise HTTPException(status_code=404, detail="item not found")

    return db_item


