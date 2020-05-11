from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, Integer, String, Sequence
from log_resource_use.src.database import add_func
"""
    The func_stats class 

    note the CPU trait will be an array [1,2,3,4]
    So iterate through the CPU array and and post new instances of the 
    func_stats object to the db per index in array
"""


class Function_Stats(declarative_base()):
    __tablename__ = 'functions'
    function = Column(String)
    id = Column(Integer, Sequence('func_id'), primary_key=True)
    cpu = Column(Float)
    duration = Column(Float)

    def __init__(self, func, cpu, duration):
        self.func = func
        self.cpu = cpu
        self.duration = duration

    def save_to_db(self):
        for x in self.cpu:
            add_func(
                Function_Stats(self.func, x, self.duration)
            )
