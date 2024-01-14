#!/usr/bin/python3
"""
    A script that creates the State “California” with the City “San Francisco”
    from the database hbtn_0e_100_usa
    Inherits from SQLAlchemy Base and links to the MySQL table cities
"""


from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    An SQL table called states
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False,
            unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
            cascade="all, delete-orphan")
