from flask import Flask, request, jsonify
from flask_cors import CORS
from dijkstras_file import Graph, dijsktra, node_coordinates  # Import your Graph class and dijsktra function
from distances_list import distances

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes by default

# Initialize the graph and add edges
graph = Graph()
edges = distances

for edge in edges:
    graph.add_edge(*edge)

# Initialize a list to store comments
comments = []

@app.route('/find_shortest_path', methods=['POST'])
def find_shortest_path():
    data = request.json
    initial = data.get('initial')
    end = data.get('end')
    
    # Call your dijsktra function
    shortest_path_geojson = dijsktra(graph, initial, end, node_coordinates)
    
    # Allow all origins for development purposes
    response = jsonify(shortest_path_geojson)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/comments', methods=['GET', 'POST'])
def handle_comments():
    if request.method == 'GET':
        response = jsonify(comments)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    elif request.method == 'POST':
        data = request.json
        comment = data.get('comment')
        if comment:
            comments.append(comment)
            response = jsonify({'message': 'Comment added successfully'})
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        else:
            response = jsonify({'error': 'Comment is required'})
            response.status_code = 400
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

if __name__ == '__main__':
    app.run(debug=True)
