# schema is the database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


username = "root"
password = "Dontwastetime1"
database_name = "store"
port = "3305"
URL_DATABASE = f"mysql+pymysql://root:{password}@localhost:{port}/{database_name}"

engine = create_engine(URL_DATABASE)

# this is database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
