from email import parser
import os
import random
from urllib.error import URLError
from QuoteEngine.ingestor import Ingestor 
from QuoteEngine.quote_gen import Quote
from MemeGenerator.MemeGenerator import MemeEngine
import argparse

# Import your Ingestor and MemeEngine classes


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]
        #debug
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        #quote = QuoteModel(body, author)
        line = body + ' - ' + author
        quote_manual = Quote(line)

    # km: tmp folder has to exist. Maybe I have to automatically create it.
    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote_manual.body, quote_manual.author)
    return path


if __name__ == "__main__":
    # @TODO Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    
    parser = argparse.ArgumentParser(description='MEME Generator\
    based on following inputs: URL, Quote, Author')

    parser.add_argument('-p', '--path', help='Insert path as "http:\\www.whatever.de\picture.jpg"')
    
    parser.add_argument('-b', '--body', help='Insert body as "Some example text"')

    parser.add_argument('-a','--author', help='Insert path as "Another Author"')

    args = parser.parse_args()
    # meme.py wird mit argumenten aufgerufen
    # Argumente
        #URL
        #Quote
        #Author

        # Haben eine Beschreibung
        # können eine Variable sein
        # können eine Funktionalität auswählen
    print('debug')
    print(args.path, args.body, args.author)

    #print(generate_meme('./_data/photos/dog/xander_1.jpg', 'My body is great', 'Author'))
    #print('debug')
    print(generate_meme(args.path, args.body, args.author))