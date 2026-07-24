from sqlmodel import SQLModel, create_engine, Session, select
from models import Task

DATABASE_URL = "sqlite:///tasks.db"
engine = create_engine(DATABASE_URL, echo=True)


def init_db() -> None:
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        existing = session.exec(select(Task)).all()
        if len(existing) == 0:
            seed_tasks = [
                Task(title="Learn SQLModel", done=False),
                Task(title="Build a CRUD API", done=False),
                Task(title="Deploy to production", done=False),
            ]
            for task in seed_tasks:
                session.add(task)
            session.commit()