from gpapp.utils.googlemaps_API import GoogleMapsApi


class TestGoogleMaps:

    def setup_method(self):
        self.gmaps = GoogleMapsApi()
        self.keywords = "tour eiffel"

    def test_http_result(self, monkeypatch):
        results = {
            "candidates": [
                {
                    'formatted_address': 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France',
                    'geometry': {'location': {'lat': 48.85837009999999,
                                              'lng': 2.2944813}}
                }
            ]
        }

        class MockRequestsResponse:
            status_code = 200

            def json(self):
                return results

        def mockreturn(url, params):
            return MockRequestsResponse()

        monkeypatch.setattr('requests.get', mockreturn)
        assert self.gmaps.get_place_location(self.keywords) == results['candidates'][0]


        # class MockRequestsResponseWith404:
        #     status_code = 404
        #
        #
        # def mockreturn(url, params):
        #     return MockRequestsResponseWith404
        #
        # self.keywords = ""
        # monkeypatch.setattr('requests.get', mockreturn)
        # assert self.gmaps.get_place_location(self.keywords) ==
