import pytest
from gpapp.utils.parser import Parser


class TestParser:
    """
    Class that tests message parser
    """

    # def setup_method(self, message):
    #     # message = "Où se trouve la Tour Eiffel ?"
    #     message = message
    #     self.parser = Parser(message)

    def test_parser(self):
        """
        test_parser method
        """
        message = "Où se trouve la Tour Eiffel ?"
        assert Parser(message).process() == "tour eiffel"

    def test_empty_string(self):
        message = " "
        with pytest.raises(ValueError):
            Parser(message).process()

    def test_stop_words(self):
        message = "Ok mais quoi alors ? !"
        with pytest.raises(ValueError):
            Parser(message).process()
