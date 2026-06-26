from unittest.mock import patch
from app.app import app

@patch("app.app.requests.get")
def test_weather_json_shape(mock_get):

    mock_get.return_value.status_code = 200

    mock_get.return_value.json.return_value = {
        "name": "London",
        "sys": {"country": "GB"},
        "main": {
            "temp": 20,
            "feels_like": 19,
            "humidity": 70
        },
        "weather": [
            {"description": "clear sky"}
        ]
    }

    client = app.test_client()

    response = client.get("/weather/London")

    data = response.get_json()

    assert response.status_code == 200

    assert "city" in data
    assert "country" in data
    assert "temperature" in data
    assert "humidity" in data
    assert "description" in data
