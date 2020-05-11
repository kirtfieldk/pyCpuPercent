"""
    Connect with SQlite DB 
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)


def add_func(func):
    Session.add(func)
    Session.commit()


"""
    Func must be an array -> this will be an array of the same function with difference cpu percent
"""


def add_all_functions(func):
    Session.add_all(func)
