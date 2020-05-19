"""
    Connect with SQlite DB 
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///func.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)


def get_session():
    return Session()


def make_tables():
    Base.metadata.create_all(engine)
