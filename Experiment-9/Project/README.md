# Experiment 9 – Efficient Bin Packing

## Aim
To implement and compare First Fit (FF), First Fit Decreasing (FFD), and Best Fit Decreasing (BFD) approximation algorithms for the Bin Packing Problem.

## Problem
Given a set of items and bins with capacity 1.0, the objective is to pack all items using the minimum possible number of bins.

## Algorithms
- **First Fit (FF):** Places each item into the first bin with enough remaining space.
- **First Fit Decreasing (FFD):** Sorts items in decreasing order and applies First Fit.
- **Best Fit Decreasing (BFD):** Sorts items in decreasing order and places each item in the bin that leaves the least remaining space.

## Sample Input
```text
Items: 0.5, 0.7, 0.3, 0.9, 0.2, 0.6, 0.8, 0.4, 0.1, 0.5
Bin Capacity: 1.0