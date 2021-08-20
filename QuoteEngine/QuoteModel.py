"""This module is reponsible  getting the body and the author"""


class QuoteModel:
    """This class is responsible for the quote and the body of the meme."""
    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __repr__(self):
        """Represent the class returning variables of constructor."""
        return f'<{self.body},-- {self.author}>'
