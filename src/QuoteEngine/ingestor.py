from typing import List
from QuoteEngine.txt_ingest import TextIngestor
from QuoteEngine.quote_gen import Quote
# Quotes importieren (muss noch erstellt werden)
# Imperator soll:
    # - In: Path
    # - Out: List with Quotes
    # data: Alle Ingestoren 
    # @Classmethod: Checken welcher Ingestor
    # - Den richtigen Ingestor "aufrufen"
    # - Eine Liste mit Quotes zurückgeben.

class Ingestor():
    ingestors = [TextIngestor]
    
    @classmethod
    def parse(cls, path: str) -> List[Quote]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):  
                return ingestor.parse(path)




# Ingestor(ABC) - Architektur eines Ingestors
    # - In: -
    # - Out: -
    # variable: Fileending
    # method: check fileending
        # IN: Path
        # OUT: TRUE / FALSE
    
    # @abstractmethod: parse
        # pass
        # return   
     

# Ingestor
    # - In: string
    # - Out: List
    # data: fileending 
    
    # IN: Path
    # OUT: List with Quotes
