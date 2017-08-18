import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

#Signals that the class is a declarative base
Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    name = Column(String)
    email = Column(String)
    picture = Column(String)
    id = Column(Integer, primary_key = True )

class Category(Base):
    """Table representing the categories of the catalog items"""
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    picture = Column(String)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {'category' : self.name, 'description' : self.description}


class CatalogItem(Base):
    """Table representing the catalog item, references the categories"""
    __tablename__ = "catalog_item"

    id = Column(Integer, primary_key = True)
    name = Column(String, nullable = False)
    description = Column(String)
    picture = Column(String)
    category_id = Column(Integer, ForeignKey("category.id"))
    category = relationship(Category)

    @property
    def serialize(self):
        #Return object in dictionary form
        return {"name": self.name,
                "category": self.category.name,
                "description": self.description}


engine = create_engine('sqlite:///catalog.db')
#Create tables from engine definition
Base.metadata.create_all(engine)
