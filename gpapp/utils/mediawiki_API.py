import requests


class MediaWikiAPI:

    def __init__(self):
        pass

    def get_page_id(self, keywords: str):
        try:
            url = "https://fr.wikipedia.org/w/api.php"
            params = {
                "action": "query",
                "list": "search",
                "srsearch": keywords,
                "srlimit": "1",
                "prop": "coordinates",
                "format": "json"
            }

            data = requests.get(url, params)
            response = data.json()['query']['search'][0]['pageid']
            return response
        except IndexError:
            return None

    def get_page_content(self, page_id: int):

        try:
            page_id = str(page_id)
            url = "https://fr.wikipedia.org/w/api.php"
            params = {
                "action": "query",
                "pageids": page_id,
                "prop": "extracts",
                "exintro": page_id,
                "exsentences": 2,
                "explaintext": "true",
                "exsectionformat": "plain",
                "format": "json"
            }

            data = requests.get(url, params)
            response = data.json()['query']['pages'][page_id]['extract']
            return response
        except KeyError:
            return None
