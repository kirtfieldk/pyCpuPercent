from sqlalchemy import Column, Float, Integer, String, Sequence
from database import Base, get_session
"""
    The func_stats class

    note the CPU trait will be an array [1,2,3,4]
    So iterate through the CPU array and and post new instances of the
    func_stats object to the db per index in array
"""


class Function_Stats(Base):
    __tablename__ = 'func'
    function = Column(String(250))
    id = Column(Integer, Sequence('func_id'), primary_key=True)
    cpu = Column(Float)
    mem = Column(Float)
    description = Column(String(250))
    home_file = Column(String(250))

    def __init__(self, func, cpu, mem, description, home_file):
        self.function = func
        self.cpu = cpu
        self.mem = mem
        self.description = description
        self.home_file = home_file

    def save_to_db(self):
        session = get_session()
        session.add(self)
        session.commit()

    def __repr__(self):
        return f"{self.function}: {self.cpu}: {self.mem} mb"
