# Metadata Header (MANDATORY)
# -----------------------------
# Program Title: Kruskal's Algorithm for MST
# Author: [@chaanakyaaM]
# Date: 2025-10-07
#
# Description: Finds the Minimum Spanning Tree (MST) of a weighted, undirected
# graph using Kruskal's algorithm, which relies on a Disjoint Set Union (DSU)
# data structure with path compression and union by rank for efficiency.
# Time Complexity: O(E log E) or O(E log V)
# Space Complexity: O(V + E)
# -----------------------------

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False  # Already in the same set

        # Union by rank
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True


def kruskal(n, edges):
    """
    n: Number of nodes (vertices)
    edges: List of edges in the format (weight, u, v)
    Returns the weight of the MST and the list of edges in the MST
    """
    # Sort edges by weight
    edges.sort()
    dsu = DisjointSet(n)
    mst = []
    total_weight = 0

    for weight, u, v in edges:
        if dsu.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    return total_weight, mst


# Example usage:
if __name__ == "__main__":
    nodes = 4
    edge_list = [
        (10, 0, 1),
        (6, 0, 2),
        (5, 0, 3),
        (15, 1, 3),
        (4, 2, 3)
    ]

    weight, mst_edges = kruskal(nodes, edge_list)
    print("Total weight of MST:", weight)
    print("Edges in MST:")
    for u, v, w in mst_edges:
        print(f"{u} -- {v} == {w}")
