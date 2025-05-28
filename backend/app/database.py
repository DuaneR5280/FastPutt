from sqlmodel import Session, create_engine, SQLModel
import time
import sqlalchemy.exc

DATABASE_URL = "postgresql://postgres:postgres@db:5432/discgolf"
engine = create_engine(DATABASE_URL, echo=True)

def create_db_and_tables():
    max_tries = 20
    for i in range(max_tries):
        try:
            SQLModel.metadata.create_all(engine)
            print("Database is ready.")
            break
        except sqlalchemy.exc.OperationalError as e:
            print(f"Database not ready yet ({i+1}/{max_tries}): {e}")
            time.sleep(2)
    else:
        raise RuntimeError("Database connection could not be established after several attempts.")


def get_session():
    with Session(engine) as session:
        yield session