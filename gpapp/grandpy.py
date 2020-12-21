from .utils.parser import Parser
from random import choice
from gpapp.utils.constants import GRANDPY_FIRST_ANSWER, GRANDPY_SECOND_ANSWER, GRANPY_WRONG_QUESTION
from gpapp.utils.mediawiki_API import MediaWikiAPI as Wiki
from gpapp.utils.googlemaps_API import GoogleMapsApi as Gmaps


class GrandPy:
    """
    Class that defines Grandpy's Answer using data
    from Google Maps and Media Wiki API's
    """

    def __init__(self):
        """
        Class constructor with GrandPy's preset data and answers in a dictionary
        """
        self.parser = Parser()
        self.wiki = Wiki()
        self.gmaps = Gmaps()
        self.answer = {
            'first_answer': choice(GRANDPY_FIRST_ANSWER),
            'second_answer': choice(GRANDPY_SECOND_ANSWER),
            'address': None,
            'lat': None,
            'lng': None,
            'place_info': None,
            'wrong_question': choice(GRANPY_WRONG_QUESTION),
            'no_wiki_info': "Désolé mon petit, je n'ai pas réussi à trouver d'informations sur ce lieu mais voici "
                            "l'adresse : "
        }

    def grandpy_answer(self, user_message: str) -> dict:
        """
        Method that sets new values to GrandPy's dictionary to return one of GrandPy's answer
        with possible place's information and location according to parsed user's input
        """

        try:
            keywords = self.parser.process(user_message)
            if keywords:
                # GoogleMaps :
                address = self.search_google(keywords)
                for data in address:
                    if data is not None:
                        self.answer['address'] = address[0]
                        self.answer['lat'] = address[1]
                        self.answer['lng'] = address[2]
                    else:
                        return self.answer
                # Wikipedia :
                info = self.search_wiki(keywords)
                info = info[0]  # Intro text of the place
                if info is not None:
                    self.answer['place_info'] = info
                else:
                    return self.answer
            return self.answer
        except TypeError:
            return self.answer

    def search_wiki(self, keywords: str):
        """
        Method that returns a possible list with place information from Wikipedia
        according to user's input
        """

        try:
            page_id = self.wiki.get_page_id(keywords)  # Place's page ID
            place_info = self.wiki.get_page_content(page_id)  # Place's intro information
            result = [place_info]
            return result
        except TypeError:
            return None

    def search_google(self, keywords: str):
        """
        Method that returns a possible list with place's location with the address,
        latitude and longitude, according to user's input
        """

        try:
            place_location = self.gmaps.get_place_location(keywords)
            address = place_location['formatted_address']  # Place's address
            coordinates = place_location['geometry']['location']
            lat = coordinates['lat']  # Place's latitude
            lng = coordinates['lng']  # Place's longitude
            result = [address, lat, lng]
            return result
        except TypeError:
            return None
