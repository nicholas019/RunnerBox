from sqlalchemy.orm import Session
from app.domain.repository.ArchiveRepository import ArchiveRepository
from app.utill.utils import get_distance_from_lat_lon_in_m


class ArchiveService:
    def __init__(self, db: Session):
        self.archive_repository = ArchiveRepository(db)

    def get_near_archive(self, latitude: float, longitude: float):
        archive_all_list = self._get_archive_all()
        result = {"subway_name": "", "exit_number": "", "location": "",
                  "start_point": {"latitude": latitude, "longitude": longitude},
                  "end_point": {"latitude": 0, "longitude": 0}, "distance": 100000}
        for archive in archive_all_list:
            distance = get_distance_from_lat_lon_in_m(latitude, longitude, archive.latitude, archive.longitude)
            if result["distance"] > distance:
                result["end_point"]["latitude"] = archive.latitude
                result["end_point"]["longitude"] = archive.longitude
                result["distance"] = distance
                result["subway_name"] = archive.subway_name
                result["exit_number"] = archive.exit_number
                result["location"] = archive.location
        return result

    def search_subway_name(self, subway_name: str):
        return self.archive_repository.get_item_by_subway_name(subway_name)

    def _get_archive_all(self):
        return self.archive_repository.get_item_all()
