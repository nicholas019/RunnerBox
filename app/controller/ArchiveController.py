from fastapi import APIRouter, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from app.config.db_config import get_db
from app.service.ArchiveService import ArchiveService

router = APIRouter()

@router.get("/archive", summary="가장가까운 물품보관소 위치정보 조회", description="<p>위도와 경도 정보를 받아 가장 가까운 물품보관소 위치정보를 반환합니다.</p> <p>쿼리 스트링으로 latitude와 longitude를 받습니다.</p> <p>ex) /archive?latitude=37.1234&longitude=127.1234</p><p> 방송통신대학교 해화 :  37.57915170946982, 127.00284721208402 </p><p> 방송통신대학교 뚝섬 :  37.54736470290424, 127.04583591769747 </p>")
async def read_item(
        latitude: float = Query(..., description="Latitude of the location"),
        longitude: float = Query(..., description="Longitude of the location"),
        db: Session = Depends(get_db)
):
    archive_service = ArchiveService(db)
    response = archive_service.get_near_archive(latitude, longitude)
    if response is None:
        raise HTTPException(status_code=404, detail="response not found")
    return response


@router.get("/archive/search", summary="지하철역 이름으로 보관소의 위치정보를 조회", description="<p>지하철역이름으로 검색하면 해당역의 물품보관소가있는 역이름과 출구번호를 반환합니다</p> <p>쿼리 스트링으로 subway를 받습니다.</p> <p>ex) /archive/search?subway_name=뚝섬역</p>")
async def read_item(
        subway_name: str = Query(..., description="subway_name"),
        db: Session = Depends(get_db)
):
    archive_service = ArchiveService(db)
    response = archive_service.search_subway_name(subway_name)
    if len(response) == 0:
        raise HTTPException(status_code=404, detail="archive not found")
    return response