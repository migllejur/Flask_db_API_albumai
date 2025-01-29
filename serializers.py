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

    @property
    def kainu_vidurkis(self) -> float:
        return round((self.kaina_online + self.kaina_store) / 2, 2)

    class Config:
        from_attributes = True