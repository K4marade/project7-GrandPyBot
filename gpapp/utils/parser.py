from gpapp.utils.constants import STOP_WORDS, ADDITIONAL_STOP_WORDS, PUNCTUATION


class Parser:
    """Class that defines application's parser"""

    def __init__(self):
        """ Class constructor """
        pass

    def process(self, message: str) -> str:
        """ Method that returns a string with only meaningful words from the user's input """

        keywords = []
        try:
            message = message.lower()
            for chars in PUNCTUATION:
                if chars in message:
                    message = message.replace(chars, " ")
            message = message.split(" ")
            for word in message:
                if word not in STOP_WORDS and word not in ADDITIONAL_STOP_WORDS:
                    keywords.append(word)
            keywords = " ".join(keywords)
            return keywords
        except ValueError:
            return keywords
