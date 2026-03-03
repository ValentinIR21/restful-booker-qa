import requests

class BookingClient:

    base_url = "https://restful-booker.herokuapp.com"

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def create_booking(self, booking_data):
        url = f"{self.base_url}/booking"

        response = self.session.post(url, json=booking_data)

        return response
        