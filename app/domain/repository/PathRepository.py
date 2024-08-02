from sqlalchemy import asc, desc
from sqlalchemy.orm import Session, joinedload

from app.domain.entity.PathEntity import WayStartListEntity, Waypoint


class PathRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_path_all(self):
        way_start_lists = (
            self.db.query(WayStartListEntity)
            .options(joinedload(WayStartListEntity.waypoints))
            .order_by(WayStartListEntity.course_index)
            .all()
        )
        for way_start_list in way_start_lists:
            way_start_list.waypoints.sort(key=lambda wp: wp.order)
        return way_start_lists

    def get_path_by_subway_name_and_exit_number(self, subway_name: str, exit_number: int):
        way_start_lists = (
            self.db.query(WayStartListEntity)
            .options(joinedload(WayStartListEntity.waypoints))
            .filter(WayStartListEntity.subway_name.like(f"%{subway_name}%"))
            .filter(WayStartListEntity.exit_number == exit_number)
            .order_by(WayStartListEntity.course_index)
            .all()
        )
        for way_start_list in way_start_lists:
            way_start_list.waypoints.sort(key=lambda wp: wp.order)

        return way_start_lists

    def get_path_by_path_id(self, path_id: int):
        way_start_lists = (
            self.db.query(WayStartListEntity)
            .options(joinedload(WayStartListEntity.waypoints))
            .filter(WayStartListEntity.id == path_id)
            .order_by(WayStartListEntity.course_index)
            .all()
        )
        for way_start_list in way_start_lists:
            way_start_list.waypoints.sort(key=lambda wp: wp.order)

        return way_start_lists
