"""
    Connect with SQlite DB 
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

metadata = MetaData()
engine = create_engine("sqlite:///func.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

"""
    Func must be an array -> this will be an array of the same function with difference cpu percent
"""
