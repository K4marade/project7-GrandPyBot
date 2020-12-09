from gpapp.utils.constants import STOP_WORDS, ADDITIONAL_STOP_WORDS, PUNCTUATION


class Parser:
    """ Class that ..."""

    def __init__(self):
        """ Class constructor """
        # self.process(message="")
        pass

    def process(self, message) -> str:
        """ Method that returns only meaningful words from the user's sentence """
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
            print(keywords)
            return keywords
        except ValueError:
            return keywords


# if __name__ == '__main__':
#     Parser()
