from datetime import date
from app.service import EventService


def test_upcoming_from_filters_events_correctly():

    service = EventService()

    service.create("Evento pasado", date(2024, 1, 1), "Madrid", "Tech")
    service.create("Evento futuro", date(2030, 1, 1), "Barcelona", "Music")

    result = service.upcoming_from(date(2025, 1, 1))

    assert len(result) == 1
    assert result[0].nombre == "Evento futuro"
