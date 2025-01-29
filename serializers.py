from pydantic import BaseModel


class AlbumasSchema(BaseModel):
    id: int
    atlikejas: str
    pavadinimas: str
    metai: int
    zanras: str
    kaina_online: float
    kaina_store: float
    kainu_vidurkis: float

    class Config:
        from_attributes = True