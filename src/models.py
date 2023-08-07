from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Characters(Base):
    __tablename__ = 'characters'
    ID = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(50))
    eye_color = Column(String(50))
    skin_color = Column(String(50))
    birth_year = Column(String(50))
    gender = Column(String(50))
    planet = Column(String(50), unique=True)

class Planets(Base):
    __tablename__ = 'planets'
    ID = Column(Integer, ForeignKey('characters.planet'), primary_key=True)
    characters = relationship(Characters)
    name = Column(String(50), nullable=False)
    diameter = Column(Integer)
    gravity = Column(String(50))
    climate = Column(String(50))
    terrain = Column(String(50))

class Starships(Base):
    __tablename__ = 'starships'
    ID = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    pilot = Column(String(50), ForeignKey('characters.ID'), unique=True)
    character = relationship(Characters)
    model = Column(String(50))
    starship_class = Column(String(50))
    manufacturer = Column(String(50))
    cost_in_credits = Column(Integer)
    length = Column(Integer)
    

class Favorites(Base):
    __tablename__ = 'favorites'
    ID = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.ID'), unique=True)
    character = relationship('Characters')
    starship_id = Column(Integer, ForeignKey('starships.ID'), unique=True)
    starship = relationship(Starships)
    planets_id = Column(Integer, ForeignKey('planets.ID'), unique=True)
    planets = relationship('Planets')

class User(Base):
    __tablename__ = 'user'
    ID = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    favorites_id = Column(Integer, ForeignKey('favorites.ID'), unique=True)
    favorite = relationship(Favorites)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
