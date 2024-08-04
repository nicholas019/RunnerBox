from fastapi import APIRouter, HTTPException, Depends,Query
from sqlalchemy.orm import Session
from app.config.db_config import get_db
from app.service.PathService import PathService

router = APIRouter()

@router.get("/path/{path_id}", summary="러닝 경로 좌표 조회", description="<p>러닝코스를 선택하면 해당 경로의 상세 경로 좌표 정보를 반환합니다</p> <p>path 정보로 추천 러닝코스의 pk값을 받습니다.</p> <p>/path/1</p>")
async def path_choice(
        path_id: int,
        db: Session = Depends(get_db)
):
    path_service = PathService(db)
    response = path_service.get_path_choice(path_id)
    if not response:
        raise HTTPException(status_code=404, detail="No paths found")
    return response

@router.get("/paths", summary="추천 코스 리스트 조회", description="<p>선택한 보관함이 있는 위치정보를 입력하면 추천 러닝코스를 반환합니다</p> <p>쿼리 스트링으로 역이름과 출구번호를 받습니다.</p> <p>/paths?subway_name=혜화역&exit_number=8</p>")
async def get_path_list(
        subway_name: str = Query(..., description="subway_name"),
        exit_number: str = Query(..., description="exit_number"),
        # distance: str = Query(..., description="distance"), # 총 뛰고 싶은 거리 입력 부분 미구현
        db: Session = Depends(get_db)
):
    path_service = PathService(db)
    response = path_service.get_path_list(subway_name, exit_number, distance=0)
    if not response:
        raise HTTPException(status_code=404, detail="No paths found")
    return response