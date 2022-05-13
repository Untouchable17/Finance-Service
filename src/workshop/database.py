from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from workshop.settings import settings

engine = create_engine(

    settings.database_url,
    connect_args={"check_same_thread": False},
)

Session = sessionmaker(
    engine, autocommit=False, autoflush=False
)


def get_session() -> Session:
    """ return db session """

    session = Session()
    try:
        yield session
    finally:
        session.close()