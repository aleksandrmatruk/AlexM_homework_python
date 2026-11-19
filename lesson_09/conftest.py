import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = ("postgresql+psycopg2://postgres:postgres@localhost:5432/"
                "QA?client_encoding=utf8")


@pytest.fixture(scope="function")
def db_session():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        yield session
    finally:
        session.close()
        engine.dispose()
