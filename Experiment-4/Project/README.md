# Smart City Emergency Route Finder using Dijkstra's Algorithm

## Project Overview

The **Smart City Emergency Route Finder** is an interactive application developed using **Dijkstra's Single Source Shortest Path Algorithm**.

The main objective of this project is to find the shortest path between different locations in a city with minimum travel distance.

The application represents the city as a weighted graph where:
- Locations are represented as vertices.
- Roads are represented as edges.
- Distance between locations is represented as edge weights.

The project uses Dijkstra's Algorithm to calculate the shortest route between a source and destination.

---

## Objective

To implement Dijkstra's Algorithm and develop a real-world application that helps find the shortest route between city locations.

---

## Features

- Interactive Graphical User Interface using Tkinter
- Select source location
- Select destination location
- Find shortest path
- Display minimum distance
- Visualize the shortest route
- Weighted graph representation
- Reset option for clearing results

---

## Technologies Used

- Python 3
- Tkinter (GUI)
- Heap Queue (`heapq`)
- Graph Data Structure
- Dijkstra's Algorithm

---

# Algorithm Used

## Dijkstra's Algorithm

Dijkstra's Algorithm is a greedy algorithm used to find the shortest path from a single source vertex to all other vertices in a weighted graph.

### Working Steps:

1. Initialize the distance of the source node as 0.
2. Initialize all other node distances as infinity.
3. Select the node with the smallest distance using a priority queue.
4. Update the distance of neighboring nodes.
5. Repeat the process until all shortest paths are found.
6. Reconstruct the path using previous nodes.

---

## Time Complexity

Using a Min-Heap priority queue:
O((V + E) log V)


Where:

- V = Number of vertices
- E = Number of edges

---

## Space Complexity


O(V)


---

# Graph Representation

The city network is represented using an adjacency list.

Example:


Hospital → School (4 km)
Hospital → Market (2 km)

School → Railway Station (5 km)

Railway Station → Airport (3 km)


---

# Example Input

Source Location:


Hospital


Destination:


Airport


---

# Example Output


Shortest Route:

Hospital → Market → School → Railway Station → Airport

Distance = 11 km


---

# How to Run

### Step 1:
Install Python 3.

### Step 2:
Open terminal inside the Project folder.

### Step 3:
Run:


python smart_route_dijkstra.py


---

# Application Areas

This project can be applied in:

- Emergency vehicle routing
- Google Maps-like navigation systems
- Transportation planning
- Smart city management
- Network routing systems

---

# Advantages

- Finds the shortest possible route efficiently.
- Reduces travel distance and time.
- Provides visual understanding of graph algorithms.
- Demonstrates real-world usage of Dijkstra's Algorithm.

---

# Conclusion

The Smart City Emergency Route Finder successfully implements Dijkstra's Single Source Shortest Path Algorithm.

The project demonstrates how graph-based algorithms can solve real-world routing problems by finding the minimum distance path between locations.

---
