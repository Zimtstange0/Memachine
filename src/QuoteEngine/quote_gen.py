
class Quote():

    def __init__(self, line: str):
        self.line = line
        self.body = str
        self.author = str

    # part = 'To bork or not to bork - Bork'
        part = self.line.split('-')
        self.body = part[0][:-1]
        self.author = part[1][1:]

    def __repr__(self):
        return f'"{self.body}" - {self.author}'