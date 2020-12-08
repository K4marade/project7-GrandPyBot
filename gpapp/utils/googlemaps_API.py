import requests

from config import GOOGLE_API_KEY
from gpapp.utils.parser import Parser


class GoogleMapsApi:

    def __init__(self):
        self.get_place_location(keywords="tour eiffel")
        pass

    def get_place_location(self, keywords):
        # try:
        url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
        params = {
            "inputtype": "textquery",
            "input": keywords,
            "fields": "formatted_address,geometry/location",
            "key": GOOGLE_API_KEY
        }
        data = requests.get(url, params)
        response = data.json()['candidates'][0]
        print(response)
        return response
    # except IndexError:
    #     return None


if __name__ == '__main__':
    GoogleMapsApi()
