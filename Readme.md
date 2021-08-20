## Python Meme Generator

This is the second project of the Udacity nanodegree python course.
This project is about generating memes.
This project consists the building of a Meme Generator()a multimedia application to dynamically generate memes, including an image with an overlaid quote)

## Data Sets
1. _data:It has 3 subfolders that are filled with photos ,quotes.
2. templates:It has HTML template files that are used for web service interactions.

## Modules
1. MemeEngine-This module helps in manipulating and drawing text. This contains a MemeEngine class which will load an image, resize it to a width of 500 pixels atmost, while maintaining the aspect ratio.
2. QuoteEngine- This module is responsible for ingesting many types of files that contain quotes. This contains an abstract base class(Ingestor interface)

## Requirements
 All the requirements for this specific project are stored in (requirements.txt).After cloning the project and entering the virtual environment run the following command:
 
  'pip install -r requirements.txt'

 # Setup
## To run this project run  the following commands  in the below order 
1. python3 -m venv env
2. source env/bin/activate
3. virtualenv flask
4. pip install -r requirements.txt 
5. cd flask
6. pip install flask

# Running the Project
1. python3 meme.py
2. python 3 app.py

NOTE:Please install "pdftotext"
Installation steps 
(To be executed in the activated virtual environment)
1. wget http://security.ubuntu.com/ubuntu/pool/main/p/poppler/libpoppler73_0.62.0-2ubuntu2.12_amd64.deb
2. sudo apt-get install ./libpoppler73_0.62.0-2ubuntu2.12_amd64.deb
3. wget http://archive.ubuntu.com/ubuntu/pool/universe/x/xpdf/xpdf_3.04-7_amd64.deb
4. sudo apt-get install ./xpdf_3.04-7_amd64.deb