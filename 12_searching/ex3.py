# Exercise 3: Binary Search (Recursive Approach)
# Description: Implement binary search using recursion
# Terminology:
#   - Recursion: Function calling itself
#   - Base Case: Condition to stop recursion
#   - Space Complexity: O(log n) due to call stack
# Example:
#   Input: [2, 3, 12, 34, 54], target=12
#   Output: Found at index 2
# Algorithm Steps:
#   1. Define base case (low > high)
#   2. Calculate mid = (low + high) // 2
#   3. Compare target with arr[mid]
#   4. Recursively search left or right half
# Advantages:
#   - Cleaner implementation
#   - Naturally follows divide-and-conquer approach
# Disadvantages:
#   - Higher space complexity
