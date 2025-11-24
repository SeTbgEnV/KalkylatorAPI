import pytest
from main import app

@pytest.fixture
def client():
    """Skapar en Flask test client."""
    with app.test_client() as client:
        yield client

@pytest.mark.parametrize(
    "payload, expected_status, expected_result",
    [
        # Normal cases with correct operators
        ({"operation": "+", "a": 2, "b": 3}, 200, 5),
        ({"operation": "-", "a": 5, "b": 2}, 200, 3),
        ({"operation": "*", "a": 3, "b": 4}, 200, 12),
        ({"operation": "/", "a": 10, "b": 2}, 200, 5),
        # Edge cases
        ({"operation": "/", "a": 10, "b": 0}, 400, None),        # Division by 0
        ({"operation": "+", "a": 1e18, "b": 1e18}, 200, 2e18),  # Large numbers
        ({"operation": "-", "a": -5, "b": -10}, 200, 5),        # Negative numbers
        ({"operation": "*", "a": 0, "b": 9999}, 200, 0),        # Multiply by 0
        ({"operation": "%", "a": 1, "b": 1}, 400, None),        # Invalid operation
        ({"operation": "+", "a": None, "b": 2}, 400, None),     # Invalid type
    ]
)

def test_calculate_endpoint(client, payload, expected_status, expected_result):
    """Tester som anropar /calculate endpoint och validerar resultat och edge cases."""
    response = client.post("/calculate", json=payload)
    assert response.status_code == expected_status
    data = response.get_json()
    if expected_result is not None:
        assert data["result"] == expected_result
    else:
        assert "error" in data