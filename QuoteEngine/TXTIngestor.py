"""This module is reponsible for the parsing of data from the given csv file"""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):

    Extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:

        if not cls.can_ingest(path):
            raise Exception('Error<<"Please recheck the file format">>')
        file = open(path, "r")
        lines = file.readlines()
        file.close()
        quotes = []
        for quote in lines:
            new_quotes = quote.rstrip("\n").split(" - ")
            if len(new_quotes) > 1:
                body = new_quotes[0]
                author = new_quotes[1]
                new_quote = QuoteModel(body, author)
                quotes.append(new_quote)

        return quotes
