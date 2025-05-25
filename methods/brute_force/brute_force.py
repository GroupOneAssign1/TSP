### Brute Force Method

The Brute Force method is the most straightforward approach to solving the Traveling Salesperson Problem (TSP). It guarantees finding the absolute shortest possible route by exhaustively examining every single possible tour.

**How it's implemented:**

1.  **Generate All Permutations:** The core of the brute force algorithm involves generating every single possible sequence (permutation) in which a salesperson can visit all cities exactly once. For a problem with 'N' cities, there are $(N-1)!$ unique tours (fixing the starting city to avoid duplicates).
2.  **Calculate Tour Distance:** For each generated permutation, the total distance of the tour is calculated by summing the distances between consecutive cities in that specific order, and finally adding the distance from the last city back to the starting city.
3.  **Identify the Shortest Tour:** The algorithm keeps track of the shortest distance found so far and the corresponding tour. After evaluating all possible permutations, the tour with the minimum total distance is identified as the optimal solution.



**Example (Conceptual):**
If there are cities A, B, C, and D, and A is the starting city, the algorithm would evaluate paths like:
* A -> B -> C -> D -> A
* A -> B -> D -> C -> A
* A -> C -> B -> D -> A
* ... and so on, for all possible orderings.# Brute Force method starter code
