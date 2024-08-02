import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.config import db_config
from app.config.init_db_data import init_db_data, clear_db_data
from app.controller import ArchiveController, PathController

app = FastAPI()

db_config.Base.metadata.create_all(bind=db_config.engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_config.database.connect()
    db = db_config.SessionLocal()
    init_db_data(db)
    db.close()
    yield
    db = db_config.SessionLocal()
    clear_db_data(db)
    db.close()
    await db_config.database.disconnect()

app = FastAPI(lifespan=lifespan)

# 여기에 실제 라우터를 추가해야 합니다. 예를 들어:
app.include_router(ArchiveController.router)
app.include_router(PathController.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
