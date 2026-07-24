from sqlmodel import Field, SQLModel
from typing import Optional


class TaskBase(SQLModel):
    title: str = Field(index=True)
    done: bool = Field(default=False)


class Task(TaskBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class TaskCreate(TaskBase):
    pass


class TaskUpdate(SQLModel):
    title: str | None = None
    done: bool | None = None


class TaskRead(TaskBase):
    id: int