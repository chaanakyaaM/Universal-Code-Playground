
# Metadata Header (MANDATORY)
# -----------------------------
# # Program Title: Floyd Warshall Algorithm
# Author: [Chaanakyaa Milkuri/@chaanakyaaM]
# Date: 2025-10-08
#
# Description: The Floyd-Warshall algorithm is an all-pairs shortest path algorithm that computes the shortest paths
# between every pair of vertices in a weighted graph. It iteratively updates the distance matrix by considering each 
# vertex as an intermediate point and checking if it offers a shorter path between two other vertices.
# Time Complexity: O(V³)
#  where V is the number of vertices in the graph.
# -----------------------------


# Solves the all-pairs shortest path
# problem using Floyd Warshall algorithm
def floydWarshall(graph):
    V = len(graph)
    INF = float('inf')  # Using infinity to represent no path

    # Add all vertices one by one to
    # the set of intermediate vertices.
    for k in range(V):

        # Pick all vertices as source one by one
        for i in range(V):

            # Pick all vertices as destination
            # for the above picked source
            for j in range(V):

                # If vertex k is on the shortest path from
                # i to j, then update the value of graph[i][j]
                if (graph[i][j] > (graph[i][k] + graph[k][j])):
                    graph[i][j] = graph[i][k] + graph[k][j]

if __name__ == "__main__":
    graph = [
        [0, 4, float('inf'), 5, float('inf')],
        [float('inf'), 0, 1, float('inf'), 6],
        [2, float('inf'), 0, 3, float('inf')],
        [float('inf'), float('inf'), 1, 0, 2],
        [1, float('inf'), float('inf'), 4, 0]
    ]
    
    floydWarshall(graph)
    for i in range(len(graph)):
        for j in range(len(graph)):
            # If the distance is infinity, print "INF" for clarity
            print("INF" if graph[i][j] == float('inf') else graph[i][j], end=" ")
        print()