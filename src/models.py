import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = 'Usuarios'
    ID = Column(Integer, primary_key=True)
    Nombre = Column(String(250))
    Apellido = Column(String(250))
    Email = Column(String)
    Contrasena = Column(String)
    Suscripcion = Column(String)
    
class Personajes(Base):
    __tablename__ = 'Personajes'
    ID = Column(Integer, primary_key=True)
    Nombre = Column(String(250))

class Planetas(Base):
    __tablename__ = 'Planetas'
    ID = Column(Integer, primary_key=True)
    Nombre = Column(String(250))

class PersonajesFavs(Base):
    __tablename__ = 'PersonajesFavs'
    ID = Column(Integer, primary_key=True)
    Usuarios_ID = Column(Integer,ForeignKey('Usuarios.ID'))
    Personajes_ID = Column(Integer,ForeignKey('Personajes.ID'))

class PlanetasFavs(Base):
    __tablename__ = 'PlanetasFavs'
    ID = Column(Integer, primary_key=True)
    Usuarios_ID = Column(Integer,ForeignKey('Usuarios.ID'))
    Planetas_ID = Column(Integer,ForeignKey('Planetas.ID'))



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')