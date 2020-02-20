import os
from flask import Flask
from flask_restful import Api
from algorithm.gensim import Gensim
from algorithm.nltk import NLTK
from algorithm.spacy import Spacy
from algorithm.summa import Summa
from algorithm.rake import Rakee

app = Flask(__name__)
api = Api(app)

api.add_resource(Gensim, '/gensim')
api.add_resource(NLTK, '/nltk')
api.add_resource(Rakee, '/rake')
api.add_resource(Spacy, '/spacy')
api.add_resource(Summa, '/summa')

if __name__ == '__main__':
    app.run(host="127.0.0.3",port="5001",debug=True)