from sqlalchemy import Column, Float, Integer, String, Sequence
from database import Base, session, engine
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
    duration = Column(Float)

    def __init__(self, func, cpu, duration, mem):
        self.function = func
        self.cpu = cpu
        self.mem = mem
        self.duration = duration

    def save_to_db(self):
        session.add(self)
        session.commit()

    def __repr__(self):
        return f"{self.function}: {self.cpu}: {self.mem} mb"
