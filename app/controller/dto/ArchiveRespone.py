from pydantic import BaseModel


class ArchiveRequest(BaseModel):
    name: str
    description: str
