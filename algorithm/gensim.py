from gensim.summarization import keywords
from flask import jsonify, request
from flask_restful import Resource

class Gensim(Resource):
    @staticmethod
    def post():
        posted_data = request.get_json()
        text = posted_data['text']
        
        text = (keywords(text).split('\n'))

        return jsonify({
            'Keywords': text
        })