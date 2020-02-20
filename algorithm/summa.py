from summa import keywords
from flask import jsonify, request
from flask_restful import Resource

class Summa(Resource):
    @staticmethod
    def post():
        posted_data = request.get_json()
        text = posted_data['text']
        
        text = (keywords.keywords(text).split('\n'))

        return jsonify({
            'Keywords': text
        })