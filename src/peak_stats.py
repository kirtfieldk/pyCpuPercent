from database import get_session, Base
from sqlalchemy import Column, Float, Integer, String, Sequence
from function_stats import Function_Stats
"""
    This table holds the unique function name as well as its duration and its highest mem usage
    and CPU usage -> If stats increase we will need to update the existing entry
"""


class Peak_Stats(Base):
    __tablename__ = 'peak_stats'
    function = Column(String(250), unique=True)
    id = Column(Integer, Sequence('func_id'), primary_key=True)
    cpu = Column(Float)
    mem = Column(Float)
    duration = Column(Float)
    description = Column(String(250))
    home_file = Column(String(250))

    def __init__(self, function, cpu, mem, duration, description, home_file):
        self.function = function
        self.cpu = cpu
        self.mem = mem
        self.duration = duration
        self.description = description
        self.home_file = home_file

    @staticmethod
    def populate_table(func, duration, home_file, description):
        session = get_session()
        res = session.query(Function_Stats).filter_by(
            function=func).all()
        largest = res[0]
        for obj in res:
            if largest.cpu < obj.cpu:
                largest = obj
        exists = session.query(Peak_Stats).filter_by(
            function=func).first()
        if exists and exists.cpu < largest.cpu:
            exists.cpu = largest.cpu
            exists.duration = largest.duration
        elif not exists:
            session.add(Peak_Stats(func, largest.cpu, largest.mem,
                                   duration, description, home_file))
        session.commit()

    def __repr__(self):
        return f"Peak Stats for {self.function}: {self.cpu}: {self.mem} mb --Duration: {self.duration}"
