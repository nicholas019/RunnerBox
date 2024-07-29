from sqlalchemy import Column, Integer, String, Float
from app.config.db_config import Base


class ArchiveEntity(Base):
    __tablename__ = "archive"
    id = Column(Integer, primary_key=True, index=True)
    subway_number = Column(Integer)
    subway_name = Column(String)
    archive_name = Column(String)
    location = Column(String)
    exit_number = Column(Integer)
    description = Column(String)
    latitude = Column(Float, index=True)
    longitude = Column(Float, index=True)