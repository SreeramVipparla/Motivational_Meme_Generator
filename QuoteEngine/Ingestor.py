from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVImporter
from .PDFIngestor import PDFImporter
from .TXTIngestor import TextIngestor


from typing import List


class Ingestor(IngestorInterface):
    """This is responsible for converting all the file\
         formats into quote reading format"""
    Ingestors = [CSVImporter, PDFImporter, DocxIngestor, TextIngestor]
# For this I have used info from the \
# knowledge post https://knowledge.udacity.com/questions/559464.

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.Ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
