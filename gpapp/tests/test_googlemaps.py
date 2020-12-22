from gpapp.utils.googlemaps_API import GoogleMapsApi
# import pytest


class TestGoogleMaps:

    def setup_method(self):
        """test setup method"""

        self.gmaps = GoogleMapsApi()

    def test_API_result(self, monkeypatch):
        """test the result of a query to Google Maps API"""

        results = {
            "candidates": [
                "formatted_address"
            ]
        }

        class MockRequestsResponse:
            status_code = 200

            def json(self):
                return results

        def mockreturn(url, params):
            return MockRequestsResponse()

        monkeypatch.setattr('requests.get', mockreturn)
        assert self.gmaps.get_place_location(
            keywords="tour eiffel") == results['candidates'][0]

        # assert self.gmaps.get_place_location(
        # keywords="mlkzeadaze:;d,eza:;d,aze:;d,") is None
        # with pytest.raises(IndexError):
        #     self.gmaps.get_place_location(keywords="?./??=:,,,,;;::::;:;:;:;::;")

        # class MockRequestsResponseWith404:
        #     status_code = 404
        #
        #
        # def mockreturn(url, params):
        #     return MockRequestsResponseWith404()
        #
        # monkeypatch.setattr('requests.get', mockreturn)
        # assert self.gmaps.get_place_location(
        # keywords="edzd;zed;ze;") == results['candidates'][0]
