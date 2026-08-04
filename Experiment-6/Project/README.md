# Matrix Optimization Assistant using Dynamic Programming

## Project Overview

The **Matrix Optimization Assistant** is an interactive application that implements the **Matrix Chain Multiplication algorithm using Dynamic Programming**.

The project finds the most efficient order of multiplying a sequence of matrices by minimizing the total number of scalar multiplications.

The application provides a graphical user interface where users can enter matrix dimensions and get the optimal multiplication order along with the minimum computation cost.

---

# Objective

To implement the Matrix Chain Multiplication problem using Dynamic Programming and develop an interactive application that finds the optimal matrix multiplication sequence.

---

# Features

- Interactive GUI using Tkinter
- Enter custom matrix dimensions
- Automatically identify matrices (A1, A2, A3...)
- Calculate minimum multiplication cost
- Display optimal parenthesization
- Generate Dynamic Programming cost table
- User-friendly dashboard interface
- Visual result presentation

---

# Technologies Used

- Python 3
- Tkinter GUI
- Dynamic Programming
- Matrix Chain Multiplication Algorithm

---

# Algorithm Used

## Matrix Chain Multiplication using Dynamic Programming

Matrix multiplication is associative, meaning the order of multiplication can be changed.

Different multiplication orders require different numbers of operations.

Dynamic Programming is used to find the order that produces the minimum number of scalar multiplications.

---

## Working Steps

1. Create a cost table `m[i][j]` to store minimum multiplication cost.
2. Divide the matrix chain into smaller sub-chains.
3. Calculate the cost for every possible splitting position.
4. Store the minimum cost and corresponding split point.
5. Reconstruct the optimal multiplication order.

---

# Time Complexity
O(n³)


where `n` is the number of matrices.

---

# Space Complexity


O(n²)


---

# Example Input

Matrix dimensions:


10 30 5 60 10


Represents:


A1 = 10 × 30

A2 = 30 × 5

A3 = 5 × 60

A4 = 60 × 10


---

# Example Output


Minimum Multiplication Cost : 27000

Optimal Parenthesization :

((A1 × A2) × (A3 × A4))

Number of Matrices : 4


---

# How to Run

### Step 1:
Install Python 3.

### Step 2:
Open terminal inside the project folder.

### Step 3:
Run:


python matrix_optimizer_gui.py


---

# Applications

Matrix Chain Multiplication optimization is used in:

- Compiler optimization
- Artificial Intelligence computations
- Computer graphics
- Scientific calculations
- Image processing
- Large-scale data processing

---

# Advantages

- Reduces unnecessary matrix multiplication operations.
- Finds the optimal multiplication order.
- Demonstrates Dynamic Programming concepts.
- Improves computational efficiency.

---

# Conclusion

The Matrix Optimization Assistant successfully implements the Matrix Chain Multiplication algorithm using Dynamic Programming.

The project demonstrates how Dynamic Programming can solve optimization problems by storing previously calculated results and selecting the best solution.

---
