from sqlalchemy import Column, Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship

from app.config.db_config import Base

class Waypoint(Base):
    __tablename__ = "waypoints"
    id = Column(Integer, primary_key=True, index=True)
    way_start_list_id = Column(Integer, ForeignKey("way_start_list.id"))
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    order = Column(Integer, nullable=False)
    distance = Column(Float, nullable=False)
    way_start_list = relationship("WayStartListEntity", back_populates="waypoints")

class WayStartListEntity(Base):
    __tablename__ = "way_start_list"
    id = Column(Integer, primary_key=True, index=True)
    course_index = Column(Integer)
    course_name = Column(String)
    subway_name = Column(String)
    exit_number = Column(Integer)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    total_distance = Column(Float, nullable=False)
    waypoints = relationship("Waypoint", back_populates="way_start_list")