// Define Node and Edge classes
class Node {
    constructor(id, name, lat, lon) {
      this.id = id;
      this.name = name;
      this.lat = lat;
      this.lon = lon;
      this.edges = []; // List to store connected edges
    }
  }
  
  class Edge {
    constructor(source, target, weight) {
      this.source = source;
      this.target = target;
      this.weight = weight;
    }
  }
  
  // Function to build graph from JSON data
  function buildGraph(data) {
    const nodes = {};
    
    // Create nodes
    data.nodes.forEach(nodeData => {
      const node = new Node(nodeData.id, nodeData.name, nodeData.lat, nodeData.lon);
      nodes[nodeData.id] = node;
    });
    
    // Create edges
    data.edges.forEach(edgeData => {
      const sourceNode = nodes[edgeData.source];
      const targetNode = nodes[edgeData.target];
      const weight = edgeData.weight;
      
      const edge = new Edge(sourceNode, targetNode, weight);
      sourceNode.edges.push(edge);
      // For undirected graph, add edge in both directions:
      // targetNode.edges.push(new Edge(targetNode, sourceNode, weight));
    });
    
    return nodes;
  }
  
  // Example JSON data
  const jsonData = {
    "nodes": [
      { "id": 1, "name": "Node 1", "lat": 40.7128, "lon": -74.0060 },
      { "id": 2, "name": "Node 2", "lat": 34.0522, "lon": -118.2437 },
      { "id": 3, "name": "Node 3", "lat": 41.8781, "lon": -87.6298 }
    ],
    "edges": [
      { "source": 1, "target": 2, "weight": 4000 },
      { "source": 2, "target": 3, "weight": 3000 },
      { "source": 1, "target": 3, "weight": 2000 }
    ]
  };
  
  // Build the graph from JSON data
  const graph = buildGraph(jsonData);
  console.log(graph);
  
  // Function to implement Dijkstra's algorithm
  function dijkstra(graph, startNodeId) {
    const distances = {};
    const visited = {};
    const queue = [];
    
    // Initialize distances and queue
    Object.values(graph).forEach(node => {
      distances[node.id] = node.id === startNodeId ? 0 : Infinity;
      visited[node.id] = false;
      queue.push(node);
    });
    
    while (queue.length > 0) {
      // Find node with the smallest distance
      queue.sort((a, b) => distances[a.id] - distances[b.id]);
      const currentNode = queue.shift();
      
      // Mark node as visited
      visited[currentNode.id] = true;
      
      // Update distances for connected nodes
      currentNode.edges.forEach(edge => {
        const neighborNode = edge.target;
        if (!visited[neighborNode.id]) {
          const newDistance = distances[currentNode.id] + edge.weight;
          if (newDistance < distances[neighborNode.id]) {
            distances[neighborNode.id] = newDistance;
          }
        }
      });
    }
    
    return distances;
  }
  
  // Example usage: Find shortest paths from Node 1 (id: 1)
  const startNodeId = 1;
  const shortestDistances = dijkstra(graph, startNodeId);
  console.log(shortestDistances);
  