import random
import os
import requests
from flask import Flask, render_template, abort, request
from MemeEngine.MemeEngine import MemeEngine
from QuoteEngine import Ingestor


app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']


    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"


    imgs = []
    for root, dir, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""

  
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']
    img = requests.get(image_url, True)
    img_file = f'tmp/{random.randint(0, 10000000)}.jpg'
    open(img_file, 'wb').write(img.content)
    path = meme.make_meme(img_file, body, author)
    os.remove(img_file)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run(host='localhost')
