# Smart City Road Network Optimization using MST

## Project Overview

The Smart City Road Network Optimization project applies **Minimum Spanning Tree (MST)** algorithms to find the minimum cost way of connecting different cities.

The project uses:
- **Kruskal's Algorithm**
- **Prim's Algorithm**

to design an optimized road network with minimum construction cost.

This application provides an interactive GUI where users can add new road connections and calculate the optimal network.

---

## Objective

To connect all cities using minimum road construction cost while ensuring every city is reachable.

---

## Features

- Interactive graphical user interface using Tkinter
- Add new city road connections
- Enter road construction cost
- Visualize city connections
- Implement Kruskal's Algorithm
- Implement Prim's Algorithm
- Display Minimum Spanning Tree
- Display minimum total construction cost
- Reset the network

---

## Technologies Used

- Python 3
- Tkinter GUI
- Graph Data Structure
- Greedy Algorithms

---

## Algorithms Used

## 1. Kruskal's Algorithm

Kruskal's algorithm is a greedy algorithm that:

1. Sorts all edges based on their weights.
2. Selects the minimum cost edge.
3. Adds the edge if it does not create a cycle.
4. Repeats until all vertices are connected.

### Time Complexity:

---

## 2. Prim's Algorithm

Prim's algorithm is a greedy algorithm that:

1. Starts from any vertex.
2. Selects the minimum cost edge connecting visited and unvisited vertices.
3. Adds the edge to the MST.
4. Continues until all vertices are included.

### Time Complexity:
## Example

Cities:


Chennai
Guindy
Adyar
Velachery
Tambaram
OMR

Road connections have different construction costs.

The program finds the minimum road network required to connect all cities.

Example Output:
Kruskal Cost = 26
Prim Cost = 26


---

## How to Run

1. Install Python 3.

2. Open terminal in the project folder.

3. Run:


python smart_city_mst.py


---

## Application

This project can be used in:

- Smart city planning
- Road construction optimization
- Network cable design
- Transportation planning
- Infrastructure cost reduction

---

## Conclusion

The project demonstrates how Minimum Spanning Tree algorithms can be applied to real-world problems. Kruskal's and Prim's algorithms help find an efficient network design with minimum cost.

---
