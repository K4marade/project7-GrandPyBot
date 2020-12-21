from gpapp.grandpy import GrandPy


class TestGranPy:
    """Class that tests GrandPy returned answer"""

    def setup_method(self):
        """Test setup method"""

        self.grandpy = GrandPy()
        self.user_message = "Peux-tu me dire où se trouve la Tour Eiffel ?"
        self.answer = {
            'first_answer': self.grandpy.answer['first_answer'],
            'second_answer': self.grandpy.answer['second_answer'],
            'address': "Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France",
            'lat': 48.85837009999999,
            'lng': 2.2944813,
            'place_info': "La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) "
                          "située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure "
                          "de la Seine dans le 7e arrondissement. Son adresse officielle est 5, avenue Anatole-France.",
            'wrong_question': self.grandpy.answer['wrong_question'],

            'no_wiki_info': "Désolé mon petit, je n'ai pas réussi à trouver d'informations sur ce lieu mais voici "
                            "l'adresse : "
        }

    def test_grandpy_answer(self):
        """Tests the returned answer of Grandpy according to user's input"""

        answer = self.grandpy.grandpy_answer(self.user_message)
        assert answer == self.answer

    def test_search_wiki(self):
        """Tests the returned result of the Wiki API"""

        keywords = "tour eiffel"
        assert self.grandpy.search_wiki(keywords) == ["La tour Eiffel  est une tour de fer puddlé de 324 mètres de "
                                                      "hauteur (avec antennes) "
                                                      "située à Paris, à l’extrémité nord-ouest du parc du "
                                                      "Champ-de-Mars en bordure "
                                                      "de la Seine dans le 7e arrondissement. Son adresse officielle "
                                                      "est 5, avenue Anatole-France."]

    def test_search_google(self):
        """Tests the returned result of the Google Maps API"""

        keywords = "tour eiffel"
        assert self.grandpy.search_google(keywords) == ["Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France",
                                                        48.85837009999999,
                                                        2.2944813]
