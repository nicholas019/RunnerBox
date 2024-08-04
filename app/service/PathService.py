from sqlalchemy.orm import Session
from app.domain.repository.PathRepository import PathRepository


class PathService:
    def __init__(self, db: Session):
        self.path_repository = PathRepository(db)

    """
    추천경로 상세정보 조회
    """
    def get_path_choice(self, path_id):
        return self.path_repository.get_path_by_path_id(path_id)

    """
    역이름과 출구번호 기준으로 추천 리스트 조회
    """
    def get_path_list(self, subway_name, exit_number, distance):
        return self.path_repository.get_path_by_subway_name_and_exit_number(subway_name, exit_number)
