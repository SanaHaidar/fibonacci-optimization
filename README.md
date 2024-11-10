# fibonacci-optimization
This repository contains optimized solutions for calculating Fibonacci sequence.
**Basic Recursion** : The naive recursive approach.
**Memoization** : A top-down dynamic porgramming approach using a cache to avoid recomputation.
**Bottom-Up** : An iterative approach that calculates Fibonacci numbers in linear sequence. 



# Problem Statement:
Calculate the nth Fibonacci number, with the following sequence definition:
-F(0) = 0
-F(1) = 1
-F(n) = F(n-1)+F(n-2) for n > 1 



# Solutions: 
-**Basic Recursion** : A straighforrward recursive implememntation of the Fibonacci sequence.
-**Memoization**: Optimized by caching previously computed Fibonacci values to reduce redundant calculations.
-**Bottom-Up Approach** : An iterative solution that computes Fibonacci values from the bottom up minimizing time and space complexity.



# Time Complexity:
-**Basic Recursion** : O(2^n) - Exponential time complexity due to repeated recursive calls for each Fibonacci number.
-**Memoization**: O(n) - Linear time complexity,since each Fibonacci number up to n is computed only once and stored.
-**Bottom-Up Approach**:(O(n) – Linear time complexity with constant space \( O(1) \) when only the last two values are kept in memory.



# To run the code, simpy execute the 'fibonacci.py' file.

```bash
python fibonacci.py 
