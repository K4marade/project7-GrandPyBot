import requests


class MediaWikiAPI:

    def __init__(self):
        # self.get_page_id(keywords="tour eiffel")
        # self.get_page_content(page_id="1359783")
        # self.get_coordinates(page_id="1359783")
        pass

    def get_page_id(self, keywords):
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
            print(response)
            return response
        except IndexError:
            return None

    def get_page_content(self, page_id):

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

    # def get_coordinates(self, page_id):
    #     page_id = str(page_id)
    #     url = "https://fr.wikipedia.org/w/api.php"
    #     params = {
    #         "action": "query",
    #         "pageids": page_id,
    #         "prop": "coordinates",
    #         "format": "json"
    #     }
    #
    #     data = requests.get(url, params)
    #     response = data.json()['query']['pages'][page_id]['coordinates'][0]
    #     return response

# if __name__ == '__main__':
#     MediaWikiAPI()
