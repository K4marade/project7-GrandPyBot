from gpapp.utils.parser import Parser


class TestParser:
    """
    Class that tests message parser
    """

    def setup_method(self):
        """ Test setup method"""
        self.parser = Parser()

    def test_parser(self):
        """
        Tests if parser returns meaningful words
        """

        message = "Où se trouve la Tour Eiffel ?"
        assert self.parser.process(message) == "tour eiffel"

    def test_empty_string(self):
        """Tests the return of an empty string"""

        message = " "
        assert self.parser.process(message) is not message

    def test_stop_words(self):
        """Tests the return if string only has stop words"""

        message = "Ok mais quoi alors ? !"
        assert self.parser.process(message) is not message
