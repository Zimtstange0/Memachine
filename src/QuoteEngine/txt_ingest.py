from ingestor_interface import IngestorInterface
# Ingestor
    # - In: string
    # - Out: List
    # data: fileending 
    
    # @classmethod --> parse
    # IN: Path
    # OUT: List with Quotes


class ingest_txt(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[quotes]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        
        quotes = []
        with open(path) as f:
            lines = f.readlines()
            for line in lines:
                
            


        return quotes