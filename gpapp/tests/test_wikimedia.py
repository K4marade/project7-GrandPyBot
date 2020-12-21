from gpapp.utils.mediawiki_API import MediaWikiAPI


class TestMediaWiki:
    """Class that tests Media Wiki API"""

    def setup_method(self):
        """Method that sets test parameters"""

        self.wiki = MediaWikiAPI()
        self.keywords = "tour eiffel"

    def test_pageid_results(self, monkeypatch):
        """Page ID test result"""

        page_id = {'query': {
            'search': [{
                'pageid': 1359783
            }]
        }}

        class MockRequestsResponse:
            status_code = 200

            def json(self):
                return page_id

        def mockreturn(url, params):
            return MockRequestsResponse()

        monkeypatch.setattr('requests.get', mockreturn)
        assert self.wiki.get_page_id(
            self.keywords) == page_id['query']['search'][0]['pageid']

    def test_content_results(self, monkeypatch):
        """Content test result from page id"""

        content = {'query': {
            'pages': {
                '1359783': {'extract': str
                            }
            }
        }}

        class MockRequestsResponse:
            status_code = 200

            def json(self):
                return content

        def mockreturn(url, params):
            return MockRequestsResponse()

        monkeypatch.setattr('requests.get', mockreturn)
        assert self.wiki.get_page_content(
            1359783) == content['query']['pages']['1359783']['extract']
