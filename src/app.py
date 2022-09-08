from genericpath import exists, isfile
import os
from re import A
from turtle import reset
import requests
import random
import shutil

from flask import Flask, render_template, abort, request
from QuoteEngine.ingestor import Ingestor 
from MemeGenerator.MemeGenerator import MemeEngine

#app = Flask(__name__)
app = Flask(__name__, static_folder='./outpic')
#meme = MemeEngine('./static')  
meme = MemeEngine('./outpic')   

def setup():
    """ Load all resources """

    #quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
    #               './_data/DogQuotes/DogQuotesDOCX.docx',
    #               './_data/DogQuotes/DogQuotesPDF.pdf',
    #               './_data/DogQuotes/DogQuotesCSV.csv']
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt']

    quotes = Ingestor.parse(quote_files[0])
    
    if 'src' in os.getcwd():
        images_path = "./_data/photos/dog/"
    else:
        images_path = r"./src/_data/photos/dog/"    
        
    # find all images within the images_path directory
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]      
    return quotes, imgs

quotes, imgs = setup()

@app.route('/')
def meme_rand():
    """ Generate a random meme """
    # select a random image from imgs array
    img = random.choice(imgs)
    
    # select a random quote from the quotes array
    quote = random.choice(quotes)

    # Generate MEME in path
    path = meme.make_meme(img, quote.body, quote.author)
    print('def meme_rand: ' + path)

    return render_template('meme.html', path=path)


@app.route('/clean', methods=['GET'])
def meme_clean():
    """ Show page with delete Button """
    return render_template('meme_clean.html')


@app.route('/create', methods=['GET'])
def meme_form():
    """ Show page with user input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    
    if request.form["pictures"] == "":
        img_url = request.form["image_url"] 
    else:
        img_url = request.form["pictures"]
        
    body = request.form["body"]
    author = request.form["author"]
    
    # 1. Use requests to save the image from the image_url
    res = requests.get(img_url, stream = True)

    with open('img.jpg', 'wb') as out_file:
        shutil.copyfileobj(res.raw, out_file)
    del res

    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    path = meme.make_meme('./img.jpg', body, author)

    # 3. Remove the temporary saved image.
    os.remove('./img.jpg')

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
    #app.run(debug=True)