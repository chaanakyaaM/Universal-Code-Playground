import heapq

def dijkstra(graph, start):
    # Priority queue to store (distance, node) pairs
    pq = [(0, start)]
    
    # Dictionary to store the shortest distance to each node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # If the current node's distance is greater than the recorded one, skip it
        if current_distance > distances[current_node]:
            continue
        
        # Explore each neighbor of the current node
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # If a shorter path is found, update the distance and push to the priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Example usage:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

print(f"Shortest paths from node {start_node}:")
for node, dist in shortest_paths.items():
    print(f"Distance to {node}: {dist}")
