from sqlalchemy.orm import Session
from app.domain.entity.ArchiveEntity import ArchiveEntity


class ArchiveRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_item_all(self):
        return self.db.query(ArchiveEntity).all()

    def get_item_by_subway_name(self, subway_name: str):
        return self.db.query(ArchiveEntity).filter(ArchiveEntity.subway_name.like(f"%{subway_name}%")).all()

