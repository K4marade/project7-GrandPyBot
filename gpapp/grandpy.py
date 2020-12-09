from .utils.parser import Parser
from random import choice
from gpapp.utils.constants import GRANDPY_FIRST_ANSWER, GRANDPY_SECOND_ANSWER, GRANPY_WRONG_QUESTION
from gpapp.utils.mediawiki_API import MediaWikiAPI as Wiki
from gpapp.utils.googlemaps_API import GoogleMapsApi as Gmaps


class GrandPy:

    def __init__(self):
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

    def grandpy_answer(self, user_message):

        try:
            keywords = self.parser.process(user_message)
            if keywords:
                # GoogleMaps :
                address = self.search_google(keywords)
                for data in address:
                    if data is not None:
                        self.answer['address'] = address[0]  # Place's address
                        self.answer['lat'] = address[1]  #
                        self.answer['lng'] = address[2]
                    else:
                        return self.answer
                # Wikipedia :
                info = self.search_wiki(keywords)
                info = info[0]  # Intro text of the place
                print(info)
                if info is not None:
                    self.answer['place_info'] = info
                else:
                    return self.answer
            return self.answer
        except TypeError:
            return self.answer

        # if coordinates from wiki and gmaps are equals :
        #       if round(info[2], 2) == round(int(self.answer['lat']), 2) and \
        #           round(info[3], 2) == round(int(self.answer['lng']), 2):

    def search_wiki(self, keywords):
        page_id = self.wiki.get_page_id(keywords)
        # Search for place's information
        place_info = self.wiki.get_page_content(page_id)
        result = [place_info]  # , lat, lon]
        print(result)
        return result

        # Search for place's coordinates to match with GoogleMaps
        # coordinates = self.wiki.get_coordinates(
        #     page_id)
        # lat = coordinates['lat']
        # lon = coordinates['lon']

    def search_google(self, keywords):

        try:
            place_location = self.gmaps.get_place_location(keywords)
            address = place_location['formatted_address']
            coordinates = place_location['geometry']['location']
            lat = coordinates['lat']
            lng = coordinates['lng']
            result = [address, lat, lng]
            return result
        except TypeError:
            return None
