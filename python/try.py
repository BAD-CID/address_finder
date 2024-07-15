from flask import Flask, request, jsonify
from flask_cors import CORS
from dijkstras_file import dijsktra, graph, node_coordinates  # Import your dijsktra function here

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes by default

# Assuming your dijsktra function is defined and imported correctly
@app.route('/find_shortest_path', methods=['POST'])
def find_shortest_path():
    data = request.json
    initial = data.get('initial')
    end = data.get('end')
    # node_coordinates = data.get('node_coordinates', {})  # Default to empty dict if not provided

    # Call your dijsktra function
    shortest_path_with_coordinates = dijsktra(graph, initial, end, node_coordinates)

    return jsonify(shortest_path_with_coordinates)

if __name__ == '__main__':
    app.run(debug=True)
