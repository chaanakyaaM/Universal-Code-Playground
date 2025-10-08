# Metadata Header (MANDATORY)
# -----------------------------
# Program Title: Bellman-Ford Shortest Path Algorithm
# Author: [IamBisrutPyne]
# Date: 2025-10-08
#
# Description: Computes the shortest path from a single source vertex to all other
# vertices in a weighted, directed graph. It successfully handles graphs with
# negative edge weights but detects and flags negative cycles.
# Time Complexity: O(V * E) (Vertices * Edges)
# Space Complexity: O(V) (for the distance array)
# -----------------------------

import math

def bellman_ford(V, edges, source):
    """
    Computes the shortest path from a source vertex using the Bellman-Ford algorithm.

    Args:
        V (int): The number of vertices (0 to V-1).
        edges (list): A list of tuples, where each tuple is (u, v, weight).
        source (int): The starting vertex (0 <= source < V).

    Returns:
        list: A list of shortest distances from the source, or None if a negative cycle is found.
    """
    # Step 1: Initialize distances from source to all other vertices as INFINITY
    # Use a large number instead of float('inf') to prevent overflow issues during addition.
    INF = float('inf')
    dist = [INF] * V
    dist[source] = 0

    # Step 2: Relax all edges V-1 times
    # This guarantees the shortest path for graphs without negative cycles.
    for i in range(V - 1):
        # Flag to optimize: if no distance changes occur, we can stop early
        relaxed_in_pass = False
        for u, v, weight in edges:
            # Only relax if the distance to 'u' is known (not INF)
            if dist[u] != INF and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                relaxed_in_pass = True
        
        # Optimization: If no distances changed in a full pass, the current distances are final
        if not relaxed_in_pass:
            break

    # Step 3: Check for negative weight cycles
    # A V-th relaxation will only succeed if a negative cycle exists.
    for u, v, weight in edges:
        if dist[u] != INF and dist[u] + weight < dist[v]:
            # This indicates a negative cycle is reachable from the source
            print("ERROR: Graph contains a negative weight cycle reachable from source.")
            return None  # Return None or handle error appropriately

    # Step 4: Return the shortest distance array
    return dist

# Example Usage:
if __name__ == "__main__":
    # Graph structure: V=6 vertices (0-5)
    # Edge format: (source, destination, weight)
    V = 6
    edge_list = [
        (0, 1, -1),
        (0, 2, 4),
        (1, 2, 3),
        (1, 3, 2),
        (1, 4, 2),
        (3, 2, 5),
        (3, 1, 1),
        (4, 3, -3),
        (4, 5, 1),
    ]
    source_node = 0

    shortest_paths = bellman_ford(V, edge_list, source_node)

    if shortest_paths is not None:
        print(f"Shortest paths from source {source_node}:")
        for i in range(V):
            dist = shortest_paths[i]
            if dist == float('inf'):
                print(f"Distance to {i}: INFINITY")
            else:
                print(f"Distance to {i}: {dist}")

    # Example 2: Negative Cycle Demonstration
    print("\n--- Testing Negative Cycle ---")
    V_cycle = 3
    edge_cycle_list = [
        (0, 1, 1),
        (1, 2, -10),
        (2, 0, 5), # This cycle (0 -> 1 -> 2 -> 0) has a total weight of 1 + (-10) + 5 = -4
    ]
    bellman_ford(V_cycle, edge_cycle_list, 0)
