from typing import List

from constants import STOP_WORDS, ADDITIONAL_STOP_WORDS


class Parser:
    """ Class that ..."""

    def __init__(self, message: str):
        """ Class constructor """

        self.message = message
        # self.process()

    def process(self) -> str:
        """ Method that returns only meaningful words from the user's sentence """

        keywords = []
        message = self.message.lower()
        message = message.replace("'", " ").replace("é", "e").replace("ê", "e").replace("è", "e")
        message = message.split(" ")
        for word in message:
            if word not in STOP_WORDS and word not in ADDITIONAL_STOP_WORDS:
                keywords.append(word)
        keywords = " ".join(keywords)

        if keywords == " " or keywords == "":
            raise ValueError("Please reformulate your question")

        print(keywords)
        return keywords


# if __name__ == '__main__':
#     Parser(message="Ok mais quoi alors ? ? !")
