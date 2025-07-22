# Exercise 2: Insertion Sort
# Description: Implement insertion sort algorithm
# Terminology:
#   - Insertion Sort: Builds final sorted array one item at a time
#   - Time Complexity: O(nÂ²) worst/average, O(n) best (already sorted)
#   - Space Complexity: O(1) (in-place)
# Algorithm Steps:
#   1. Start with second element (consider first element as sorted)
#   2. Compare with previous elements and insert at correct position
#   3. Repeat for all elements
# Example:
#   Input: [12, 11, 13, 5, 6]
#   Process:
#     Pass 1: [12, 11, 13, 5, 6]
#     Pass 2: [11, 12, 13, 5, 6]
#     Pass 3: [5, 11, 12, 13, 6]
#     Pass 4: [5, 6, 11, 12, 13]
#   Output: [5, 6, 11, 12, 13]
