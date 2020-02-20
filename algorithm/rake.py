from multi_rake import Rake
from flask import jsonify, request
from flask_restful import Resource

class Rakee(Resource):
    @staticmethod
    def post():
        posted_data = request.get_json()
        text = posted_data['text']
        rake = Rake()
        keywords = rake.apply(text)
        text = [i[0] for i in keywords]

        return jsonify({
            'Keywords': text
        })