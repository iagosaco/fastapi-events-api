from fastapi import FastAPI
from datetime import date
from .models import EventCreate
from .service import event_service

app = FastAPI()


@app.post("/events")
def create_event(event: EventCreate):
    return event_service.create(
        event.nombre,
        event.fecha,
        event.ciudad,
        event.tipo
    )


@app.get("/events/upcoming")
def get_upcoming_events(from_date: date):
    return event_service.upcoming_from(from_date)
