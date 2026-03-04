import pytest
from clients.booking_client import BookingClient
from data.test_data import *
import allure

@pytest.fixture
def client():

    client = BookingClient()

    return client

@allure.feature("Booking Management")
@allure.story("Create Booking")

def test_booking_passed(client):
    
    response = client.create_booking(valid_booking_data)
    
    assert response.status_code != 500
    
    assert response.status_code == 200
    
    data = response.json()
    assert "bookingid" in data, "Нет bookingid в ответе"
    assert "booking" in data, "Нет данных брони в ответе"
    
    booking = data["booking"]
    assert booking["firstname"] == valid_booking_data["firstname"]
    assert booking["lastname"] == valid_booking_data["lastname"]
    assert booking["totalprice"] == valid_booking_data["totalprice"]

def test_booking_missing_firstname(client):

    response = client.create_booking(missing_firstname_data)

    assert response.status_code != 500,\
        f"server has dropped from 500. Статус: {response.status_code}"
    
    assert response.status_code == 400, \
        f"Expected 400, but it came: {response.status_code}"
    
    data = response.json()

    assert "error" in data or "reason" in data, "Нет описания ошибки"

def test_booking_empty_firstname(client):

    response = client.create_booking(empty_firstname_data)

    assert response.status_code != 500,\
        f"server has dropped from 500. Статус: {response.status_code}"
    
    assert response.status_code == 400, \
        f"Expected 400, but it came: {response.status_code}"
    
    data = response.json()

    assert "error" in data or "reason" in data, "Нет описания ошибки"

def test_booking_empty_checkin(client):

    response = client.create_booking(empty_checkin_data)

    assert response.status_code != 500,\
        f"server has dropped from 500. Статус: {response.status_code}"
    
    assert response.status_code == 400, \
        f"Expected 400, but it came: {response.status_code}"
    

    
