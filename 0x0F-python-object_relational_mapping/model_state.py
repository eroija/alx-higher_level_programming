#!/usr/bin/python3
"""
   contains the class definition of a State and an instance
   Base = declarative_base():
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(base):

    """
       it represents a state for the mysql database
       __tablename__: name of mysql table to store states.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
