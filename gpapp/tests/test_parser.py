from gpapp.utils.parser import Parser


class TestParser:
    """
    Class that tests message parser
    """

    def setup_method(self):
        self.parser = Parser()

    def test_parser(self):
        """
        test_parser method
        """
        message = "Où se trouve la Tour Eiffel ?"
        assert self.parser.process(message) == "tour eiffel"

    def test_empty_string(self):
        message = " "
        assert self.parser.process(message) is not message

    def test_stop_words(self):
        message = "Ok mais quoi alors ? !"
        assert self.parser.process(message) is not message
