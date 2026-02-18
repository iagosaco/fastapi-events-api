import httpx

BASE_URL = "http://127.0.0.1:8000"


def test_create_event_e2e():

    response = httpx.post(
        f"{BASE_URL}/events",
        json={
            "nombre": "Concierto",
            "fecha": "2030-06-01",
            "ciudad": "Valencia",
            "tipo": "Music"
        }
    )

    assert response.status_code == 200
    assert response.json()["nombre"] == "Concierto"


def test_get_upcoming_events_e2e():

    response = httpx.get(
        f"{BASE_URL}/events/upcoming?from_date=2025-01-01"
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)
