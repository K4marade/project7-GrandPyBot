from gpapp.grandpy import GrandPy


class TestGranPy:
    """Class that tests GrandPy returned answer"""

    def setup_method(self):
        """Test setup method"""

        self.grandpy = GrandPy()
        self.answer = {
            'first_answer': self.grandpy.answer['first_answer'],
            'second_answer': self.grandpy.answer['second_answer'],
            'address': "Champ de Mars, 5 Avenue Anatole France, "
                       "75007 Paris, France",
            'lat': 48.85837009999999,
            'lng': 2.2944813,
            'place_info': "La tour Eiffel  est une tour de fer puddlé de "
                          "324 mètres de hauteur (avec antennes) "
                          "située à Paris, à l’extrémité nord-ouest du "
                          "parc du Champ-de-Mars en bordure "
                          "de la Seine dans le 7e arrondissement. "
                          "Son adresse officielle est "
                          "5, avenue Anatole-France.",
            'wrong_question': self.grandpy.answer['wrong_question'],

            'no_wiki_info': "Désolé mon petit, je n'ai pas réussi "
                            "à trouver d'informations sur ce lieu mais voici "
                            "l'adresse : ",
        }

    def test_grandpy_answer(self):
        """Tests the returned answer of Grandpy according to user's input"""

        answer_ok = self.grandpy.grandpy_answer(
            user_message="Peux-tu me dire où se trouve la Tour Eiffel ?")
        assert answer_ok == self.answer

        # No info received from API's
        answer_ko = self.grandpy.grandpy_answer(user_message="=;@=:@;=@;@:=;@")
        assert answer_ko == self.answer

    def test_search_wiki(self):
        """Tests the returned result of the Wiki API"""

        assert self.grandpy.search_wiki(keywords="tour eiffel") == [
            "La tour Eiffel  est une tour de fer puddlé de 324 mètres de "
            "hauteur (avec antennes) "
            "située à Paris, à l’extrémité nord-ouest du parc du "
            "Champ-de-Mars en bordure "
            "de la Seine dans le 7e arrondissement. Son adresse officielle "
            "est 5, avenue Anatole-France."
        ]
        assert self.grandpy.search_wiki(
            keywords=":;,:;@,@:;,@@@") is not self.answer

    def test_search_google(self):
        """Tests the returned result of the Google Maps API"""

        assert self.grandpy.search_google(keywords="tour eiffel") == [
            "Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France",
            48.85837009999999,
            2.2944813
        ]
        assert self.grandpy.search_google(keywords=":;,:;@,@:;,@@@") is None
