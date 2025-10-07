import heapq

def prim(graph, start_vertex=0):
    """
    Implements Prim's Algorithm to find the Minimum Spanning Tree (MST) of a graph.
    
    :param graph: Adjacency list representation of the graph (dictionary of dictionaries)
    :param start_vertex: The starting vertex for the algorithm
    :return: A tuple containing (MST cost, MST edges)
    """
    
    # Initialize the MST and necessary data structures
    mst_cost = 0
    mst_edges = []
    visited = set()
    min_heap = [(0, start_vertex)]  # (edge weight, vertex)
    
    while min_heap:
        weight, vertex = heapq.heappop(min_heap)
        
        # Skip if the vertex is already included in the MST
        if vertex in visited:
            continue
        
        # Include the vertex in the MST
        visited.add(vertex)
        mst_cost += weight
        
        if weight != 0:
            mst_edges.append((last_vertex, vertex, weight))
        
        # Add the neighboring vertices and their edge weights to the priority queue
        for neighbor, edge_weight in graph[vertex].items():
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor))
        
        last_vertex = vertex  

    return mst_cost, mst_edges

graph = {
    0: {1: 2, 3: 6},
    1: {0: 2, 2: 3, 3: 8, 4: 5},
    2: {1: 3, 4: 7},
    3: {0: 6, 1: 8},
    4: {1: 5, 2: 7}
}

cost, mst = prim(graph)
print(f"MST Cost: {cost}")
print("MST Edges:", mst)
