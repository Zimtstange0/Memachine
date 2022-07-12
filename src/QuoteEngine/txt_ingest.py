from typing import List
from QuoteEngine.ingestor_interface import IngestorInterface
from QuoteEngine.quote_gen import Quote
import re

# Ingestor
    # - In: string
    # - Out: List
    # data: fileending 
    
    # @classmethod --> parse
    # IN: Path
    # OUT: List with Quotes


class TextIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        quotes = []
        with open(path) as f:
            lines = f.readlines()
            for line in lines:
                # delete "ï»¿". Beginning of some ascii files
                line = re.sub("ï»¿", "", line)
                quotes.append(Quote(line))

        return quotes