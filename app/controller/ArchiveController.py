from fastapi import APIRouter, HTTPException, Query, Depends
from sqlalchemy.orm import Session
from app.config.db_config import get_db
from app.service.ArchiveService import ArchiveService

router = APIRouter()



@router.get("/archive")
async def read_item(
        latitude: float = Query(..., description="Latitude of the location"),
        longitude: float = Query(..., description="Longitude of the location"),
        db: Session = Depends(get_db)
):
    archive_service = ArchiveService(db)
    item = archive_service.get_near_archive(latitude, longitude)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.get("/archive/search")
async def read_item(
        subway_name: str = Query(..., description="subway_name"),
        db: Session = Depends(get_db)
):
    archive_service = ArchiveService(db)
    item = archive_service.search_subway_name(subway_name)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item