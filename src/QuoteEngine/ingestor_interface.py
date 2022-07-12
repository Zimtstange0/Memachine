from typing import List
from abc import ABC, abstractmethod
from QuoteEngine.quote_gen import Quote
# Ingestor(ABC) - Architektur eines Ingestors
    # - In: -
    # - Out: -
    # variable: Fileending
    # method: check fileending
        # IN: Path
        # OUT: TRUE / FALSE
    
    # @abstractmethod: parse
        # pass
   
class IngestorInterface(ABC):
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[Quote]:
        pass
