import requests

from config import GOOGLE_API_KEY


class GoogleMapsApi:
    """
    Class that uses Google Maps API to get place's location to display it
    with GoogleMaps
    """

    def __init__(self):
        """Class constructor"""
        # self.get_place_location(keywords="mlkzeadaze:;d,eza:;d,aze:;d,")
        pass

    def get_place_location(self, keywords: str):
        """
        Methods that gets place's location from the API with
        its address, latitude and longitude
        """

        # try:
        url = "https://maps.googleapis.com/maps/api/" \
              "place/findplacefromtext/json"
        params = {
            "inputtype": "textquery",
            "input": keywords,
            "fields": "formatted_address,geometry/location",
            "key": GOOGLE_API_KEY,
            "language": "fr"
        }
        data = requests.get(url, params)
        response = data.json()['candidates'][0]
        return response
    # except (IndexError, TypeError):
        #     return None


# if __name__ == '__main__':
#     GoogleMapsApi()
