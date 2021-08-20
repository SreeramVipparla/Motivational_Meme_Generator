"""This module is reponsible \
for the parsing of data from the given docx file"""
from typing import List
import docx
import subprocess

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    Extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Error<<"Please recheck the file format">>')
        quotes = []
        documentextended = docx.Document(path)
        for paragraph in documentextended.paragraphs:
            if paragraph.text != "":
                parse = paragraph.text.split('-')
                updated_quote = QuoteModel(parse[0], parse[1])
                quotes.append(updated_quote)

        return quotes
