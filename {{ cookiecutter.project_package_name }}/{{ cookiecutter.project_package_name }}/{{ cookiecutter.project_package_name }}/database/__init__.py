from settings import settings
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()
engine = create_engine(settings.database_uri)
Session.configure(bind=engine)


Base = declarative_base()
Base.metadata.bind = engine


def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
