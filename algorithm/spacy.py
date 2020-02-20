from gensim.summarization import keywords
from flask import jsonify, request
from flask_restful import Resource

class Spacy(Resource):
    @staticmethod
    def post():
        posted_data = request.get_json()
        text = posted_data['text']
        
        text = (keywords(text))

        return jsonify({
            'Keywords': text
        })