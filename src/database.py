"""
    Connect with SQlite DB 
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import sqlite3

metadata = MetaData()
engine = create_engine("sqlite:///func.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

