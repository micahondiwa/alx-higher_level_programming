#!/usr/bin/python3
"""
States calss and Base, and instance of declarative_base()
"""
from sqlalchemy import column, Integer, String, MetaData
from sqlalchemy.ext.declative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """
    class with id and name attributes for every state
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
