import nltk
from flask import jsonify, request
from flask_restful import Resource

class NLTK(Resource):
    @staticmethod
    def post():
        posted_data = request.get_json()
        text = posted_data['text']
        tokenized = nltk.word_tokenize(text)
        pos_tagged = nltk.pos_tag(tokenized)
        chunked = nltk.chunk.ne_chunk(pos_tagged, binary=False)
        continuous_chunk = []
        current_chunk = []
        for i in chunked:
            if type(i) == nltk.tree.Tree:
                current_chunk.append(" ".join([token for token, pos in i.leaves()]))
            elif current_chunk:
                named_entity = " ".join(current_chunk)
                if named_entity not in continuous_chunk:
                    continuous_chunk.append(named_entity)
                    current_chunk = []
            else:
                continue

        return jsonify({
            'Keywords': continuous_chunk
        })