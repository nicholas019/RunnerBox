from fastapi import APIRouter, HTTPException, Depends,Query
from sqlalchemy.orm import Session
from app.config.db_config import get_db
from app.service.PathService import PathService

router = APIRouter()

@router.get("/path/{path_id}")
async def path_choice(
        path_id: int,
        db: Session = Depends(get_db)
):
    path_service = PathService(db)
    response = path_service.get_path_choice(path_id)
    if not response:
        raise HTTPException(status_code=404, detail="No paths found")
    return response

@router.get("/paths")
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