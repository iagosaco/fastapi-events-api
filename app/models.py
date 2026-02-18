from pydantic import BaseModel
from datetime import date


class Event(BaseModel):
    id: int
    nombre: str
    fecha: date
    ciudad: str
    tipo: str


class EventCreate(BaseModel):
    nombre: str
    fecha: date
    ciudad: str
    tipo: str
