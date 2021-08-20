"""Extracting the data from PDF files."""

from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFImporter(IngestorInterface):
    Extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse data from pdf using pdftotext subprocess."""
        if not cls.can_ingest(path):
            raise Exception('Error<<"Please recheck the file format">>')

        tmp = f'./tmp_{random.randint(0,1000000)}.txt'
        subprocess.call(['pdftotext', path, tmp])
# please refer(https://knowledge.udacity.com/questions/633566) for the above two commands.
        file_ref = open(tmp, "r")
        quotes = []
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split('-')
                quotes.append(QuoteModel(parsed[0].strip(), parsed[1].strip()))
        file_ref.close()
        os.remove(tmp)
        return quotes
