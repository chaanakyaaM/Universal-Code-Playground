/**
 * -----------------------------
 * Program Title: Dijkstra's Shortest Path Algorithm
 * Author: [Sreenivasulu-03]
 * Date: 2025-10-07
 *
 * Description: Finds the shortest path from a starting node to all other nodes
 * in a weighted, directed graph using a priority queue (min-heap).
 * Demonstrates efficient graph traversal and shortest path computation.
 *
 * Time Complexity: O(E log V)
 * Space Complexity: O(V + E)
 * -----------------------------
 */

import java.util.*;

public class DijkstraAlgorithm {

    /**
     * Inner class representing an edge with a destination vertex and weight.
     */
    static class Edge {
        int dest;
        int weight;

        Edge(int dest, int weight) {
            this.dest = dest;
            this.weight = weight;
        }
    }

    /**
     * Performs Dijkstra's algorithm to find shortest paths from a source vertex.
     *
     * @param graph  The adjacency list representing the graph.
     * @param source The starting vertex.
     * @return A map containing the shortest distance to each vertex.
     */
    public static Map<Integer, Integer> dijkstra(Map<Integer, List<Edge>> graph, int source) {
        // Priority queue to store (distance, vertex) pairs
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));

        // Stores shortest known distances to each vertex
        Map<Integer, Integer> distances = new HashMap<>();
        for (int node : graph.keySet()) {
            distances.put(node, Integer.MAX_VALUE);
        }
        distances.put(source, 0);
        pq.add(new int[]{0, source});

        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int currentDistance = current[0];
            int currentNode = current[1];

            // Skip if we already found a shorter path
            if (currentDistance > distances.get(currentNode)) continue;

            // Explore neighbors
            for (Edge edge : graph.getOrDefault(currentNode, new ArrayList<>())) {
                int newDist = currentDistance + edge.weight;
                if (newDist < distances.get(edge.dest)) {
                    distances.put(edge.dest, newDist);
                    pq.add(new int[]{newDist, edge.dest});
                }
            }
        }

        return distances;
    }

    /**
     * Driver method to take input, build the graph, and display shortest paths.
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of vertices: ");
        int vertices = sc.nextInt();

        System.out.print("Enter number of edges: ");
        int edges = sc.nextInt();

        Map<Integer, List<Edge>> graph = new HashMap<>();
        for (int i = 0; i < vertices; i++) {
            graph.put(i, new ArrayList<>());
        }

        System.out.println("Enter edges in format: source destination weight");
        for (int i = 0; i < edges; i++) {
            int src = sc.nextInt();
            int dest = sc.nextInt();
            int weight = sc.nextInt();
            graph.get(src).add(new Edge(dest, weight));
        }

        System.out.print("Enter source vertex: ");
        int source = sc.nextInt();

        Map<Integer, Integer> shortestPaths = dijkstra(graph, source);

        System.out.println("\nShortest paths from vertex " + source + ":");
        for (int node : shortestPaths.keySet()) {
            int dist = shortestPaths.get(node);
            System.out.println("Vertex " + node + " → Distance: " + (dist == Integer.MAX_VALUE ? "∞" : dist));
        }

        sc.close();
    }
}
