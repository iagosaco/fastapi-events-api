from datetime import date
from .models import Event


class EventService:

    def __init__(self):
        self.events = []
        self.current_id = 1

    def create(self, nombre: str, fecha: date, ciudad: str, tipo: str) -> Event:
        event = Event(
            id=self.current_id,
            nombre=nombre,
            fecha=fecha,
            ciudad=ciudad,
            tipo=tipo
        )
        self.events.append(event)
        self.current_id += 1
        return event

    def upcoming_from(self, from_date: date) -> list[Event]:
        return [
            event for event in self.events
            if event.fecha > from_date
        ]


event_service = EventService()
