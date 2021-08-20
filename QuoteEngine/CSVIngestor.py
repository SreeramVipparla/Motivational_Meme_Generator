"""This module is reponsible for the parsing of data from the given csv file"""

from typing import List
import pandas as pd

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVImporter(IngestorInterface):
    """This function parses the csv information """

    Extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """This parses the data from rows as body and author"""
        if not cls.can_ingest(path):
            raise Exception('Error<<"Please recheck the file format">>')

        quotes = []
        df = pd.read_csv(path, header=0)

        for row in df.iterrows():
            quote, author = row
            quotes.append(QuoteModel(quote, author))

        return quotes
