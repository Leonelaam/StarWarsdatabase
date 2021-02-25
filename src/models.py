import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# mis tablas StaWars
class User(Base):
    __tablename__ = "user"
    uid = Column(Integer, primary_key=True)
    first_name = Column(String(20)) 
    second_name = Column(String(20))
    email = Column(String(20), unique=True, nullable=False)
    password = Column(String(20), nullable=False)
    fav_characters = relationship("Favorite_Character")
    fav_vehicles = relationship("Favorite_Vehicle")
    fav_planets = relationship("Favorite_Planet")

class Character(Base):
    __tablename__ = "character"
    uid = Column(Integer, primary_key=True)
    name = Column(String(20)) 
    height = Column(Float)
    mass = Column(Float)
    hair_color = Column(String(20)) 
    skin_color = Column(String(20)) 
    eye_color = Column(String(20)) 
    birth_year = Column(Date) 
    gender = Column(String(20)) 
    created = Column(Date) 
    edited = Column(Date) 
    homeworld = Column(String(20))
    like_by_users = relationship("Favorite_Character")

class Planet(Base):
    __tablename__= "planet"
    uid = Column(Integer, primary_key=True)
    name = Column(String(20))
    diameter = Column(Float)
    rotation_period = Column(Float)
    orbital_period = Column(Float)
    gravity = Column(Float)
    population = Column(Integer)
    climate = Column(String(20))
    terrain = Column(String(20))
    surface_water = Column(Integer)
    created = Column(Date)
    edited = Column(Date)
    like_by_users = relationship("Favorite_Planet")

class Vehicle(Base):
    __tablename__ = "vehicle"
    uid = Column(Integer, primary_key=True)
    name = Column(String(20)) 
    model = Column(String(20)) 
    starship_class = Column(String(20)) 
    manufacturer = Column(String(20)) 
    cost_in_credits = Column(Integer) 
    length = Column(Float) 
    crew = Column(Float) 
    passengers = Column(Integer) 
    max_atmosphering_speed = Column(Float) 
    hyperdrive_rating = Column(Float) 
    mglt = Column(Integer) 
    cargo_capacity = Column(Integer) 
    consumables = Column(String(20)) 
    pilots = Column(Integer) 
    created = Column(Date)
    edited = Column(Date)
    like_by_users = relationship("Favorite_Vehicle")


class Favorite_Character(Base):
    __tablename__= "favorite_character"
    uid = Column(Integer, primary_key=True)
    user_uid = Column(Integer, ForeignKey('user.uid'))
    character_uid = Column(Integer, ForeignKey('character.id'))

class Favorite_Vehicle(Base):
    __tablename__= "favorite_vehicle"
    uid = Column(Integer, primary_key=True)
    user_uid = Column(Integer, ForeignKey('user.uid'))
    vehicle_uid = Column(Integer, ForeignKey('vehicle.uid'))

class Favorite_Planet(Base):
    __tablename__= "favorite_planet"
    uid = Column(Integer, primary_key=True)
    user_uid = Column(Integer, ForeignKey('user.uid'))
    planet_uid = Column(Integer, ForeignKey('planet.uid'))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')