# Smart Data Analyzer using Divide and Conquer Min-Max Algorithm

## Project Overview

Smart Data Analyzer is an interactive Python application that finds the **minimum and maximum values** from a dataset using the **Divide and Conquer technique**.

Instead of checking every element repeatedly, the algorithm divides the dataset into smaller parts, finds the minimum and maximum values of each part, and combines the results efficiently.

This project provides a graphical user interface (GUI) to demonstrate the working of the algorithm in a simple and visual way.

---

## Objective

To implement the Divide and Conquer technique for finding minimum and maximum values from an array and demonstrate its efficiency through an interactive application.

---

## Features

- Interactive GUI using Tkinter
- Enter custom datasets
- Generate random datasets
- Find minimum value
- Find maximum value
- Count number of comparisons performed
- Visualize dataset using bar graph
- Highlight minimum and maximum values
- Simple and user-friendly interface

---

## Technologies Used

- Python 3
- Tkinter (GUI)
- Divide and Conquer Algorithm
- Recursion
- Data Visualization using Tkinter Canvas

---

# Algorithm Used

## Divide and Conquer Min-Max Algorithm

The algorithm divides the given array into two halves recursively.

### Steps:

1. Divide the array into two smaller sub-arrays.
2. Find minimum and maximum values of each half recursively.
3. Compare the two minimum values to find the overall minimum.
4. Compare the two maximum values to find the overall maximum.
5. Return the final minimum and maximum values.

---

## Time Complexity
O(n)


The algorithm visits every element once while reducing the number of comparisons.

---

## Comparison Count

For an array of size `n`, the number of comparisons is:


3n/2 - 2


This is more efficient compared to the normal approach:


2(n-1)


---

# Working Example

### Input:


45,12,78,3,90,25,67,10


### Output:


Minimum Value : 3

Maximum Value : 90

Comparisons Used : 10

Algorithm : Divide & Conquer


---

# How to Run

### Step 1:
Install Python 3.

### Step 2:
Open terminal inside the project folder.

### Step 3:
Run:


python smart_minmax_analyzer.py


---

# Applications

This project can be applied in:

- Data analysis systems
- Finding highest and lowest scores
- Temperature monitoring systems
- Stock market analysis
- Sensor data processing
- Large dataset processing

---

# Advantages

- Requires fewer comparisons than the traditional method.
- Efficient for large datasets.
- Demonstrates recursion and divide-and-conquer concepts.
- Provides visual understanding of algorithm execution.

---

# Conclusion

The Smart Data Analyzer successfully implements the Divide and Conquer Min-Max algorithm.

The project demonstrates how dividing a problem into smaller sub-problems can improve efficiency and reduce unnecessary comparisons while finding minimum and maximum values.

---
