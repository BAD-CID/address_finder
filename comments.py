from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

comments = []

@app.route('/comments', methods=['GET'])
def get_comments():
    return jsonify(comments)

@app.route('/comments', methods=['POST'])
def add_comment():
    comment = request.json.get('comment')
    if comment:
        comments.append(comment)
        return jsonify({'message': 'Comment added!'}), 201
    return jsonify({'error': 'Comment is required'}), 400

if __name__ == '__main__':
    app.run(debug=True)
