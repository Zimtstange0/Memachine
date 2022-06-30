from abc import ABC, abstractmethod

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
    def can_ingest(cls, path: str) -> boolean:
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
