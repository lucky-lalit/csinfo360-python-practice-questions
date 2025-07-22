# Exercise 2: Binary Search
# Description: Implement binary search algorithm (iterative approach)
# Terminology:
#   - Binary Search: Divide and conquer algorithm
#   - Time Complexity: O(log n)
#   - Space Complexity: O(1) for iterative approach
# Prerequisite: Array must be sorted
# Example:
#   Input: [2, 3, 12, 34, 54], target=34
#   Output: Found at index 3
# Algorithm Steps:
#   1. Compare target with middle element
#   2. If matches, return index
#   3. If target greater, search right half
#   4. If target smaller, search left half
#   5. Repeat until found or search space exhausted
# Advantages:
#   - Much faster than linear search for large datasets
# Disadvantages:
#   - Requires sorted array
#   - More complex implementation
