from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# DATABASE_URL = settings.db_url

DATABASE_URL='postgresql://postgres:ags009@localhost:5432/worldcup23'

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def CreateTables():
     Base.metadata.create_all(bind=engine)


def get_db():
     db = SessionLocal()
     try:
          yield db
     finally:
          db.close()