from sqlalchemy.orm import Session
from app.domain.repository.ArchiveRepository import ArchiveRepository
from app.utill.utils import get_distance_from_lat_lon_in_m


class ArchiveService:
    def __init__(self, db: Session):
        self.archive_repository = ArchiveRepository(db)

    """
    메인 페이지에서 가장 가까운 지하철 역을 찾는 함수
    """
    def get_near_archive(self, latitude: float, longitude: float):
        archive_all_list = self._get_archive_all()

        return self._format_location(archive_all_list, latitude, longitude)

    """
    역이름으로 보관소 위치 검색
    """
    def search_subway_name(self, subway_name: str):
        return self.archive_repository.get_archive_by_subway_name(subway_name)

    """
    모든 보관소 리스트 조회
    """
    def _get_archive_all(self):
        return self.archive_repository.get_archive_all()

    """
    거리측정 결과 포맷팅 함수
    """
    @staticmethod
    def _format_location(archive_all_list, latitude, longitude):
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
