# String Matching Comparison

## Project Description

This project demonstrates a comparative analysis of three popular string matching algorithms:

* Naive String Matching
* Rabin-Karp Algorithm
* Knuth-Morris-Pratt (KMP) Algorithm

The application allows users to enter a text and a search pattern through a simple graphical user interface (GUI). It searches for the pattern using all three algorithms, displays the matching positions, measures the execution time of each algorithm, and identifies the fastest algorithm for the given input.

## Objectives

* Implement three string matching algorithms in Python.
* Compare their execution times.
* Display the positions where the pattern is found.
* Identify the fastest algorithm for the given input.
* Provide a simple and user-friendly GUI using Tkinter.

## Features

* User-friendly graphical interface.
* Text box for entering the input text.
* Text box for entering the search pattern.
* Pattern matching using:

  * Naive Algorithm
  * Rabin-Karp Algorithm
  * KMP Algorithm
* Displays all matching index positions.
* Measures and compares execution time.
* Highlights the fastest algorithm for the current input.

## Technologies Used

* Python 3
* Tkinter (GUI)
* Time Module

## Algorithms Used

### 1. Naive String Matching

Compares the pattern with every possible position in the text until a match is found.

**Time Complexity:** O(n × m)

### 2. Rabin-Karp Algorithm

Uses a hashing technique to efficiently compare the pattern with the text.

**Average Time Complexity:** O(n + m)

### 3. Knuth-Morris-Pratt (KMP) Algorithm

Uses the Longest Prefix Suffix (LPS) array to avoid unnecessary comparisons.

**Time Complexity:** O(n + m)

## How to Run

1. Open the project folder.
2. Run the following command:

```bash
python string_matching_comparison.py
```

3. Enter the text and pattern.
4. Click the **Analyze Algorithms** button.
5. View:

   * Match positions
   * Execution time of each algorithm
   * Fastest algorithm

## Sample Input

**Text**

```
Data Structures and Algorithms are important in Computer Science
```

**Pattern**

```
Algorithms
```

## Sample Output

```
Naive Algorithm
Matches: [20]
Execution Time: 0.000021 seconds

Rabin-Karp Algorithm
Matches: [20]
Execution Time: 0.000015 seconds

KMP Algorithm
Matches: [20]
Execution Time: 0.000011 seconds

Fastest Algorithm: KMP
```

> **Note:** The fastest algorithm may vary depending on the length and content of the text and pattern.

## Project Structure

```
Experiment-2
│
├── EXP2_string_matching.py
│
└── Project
    ├── string_matching_comparison.py
    └── README.md
```

git status
