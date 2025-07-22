# Exercise 6: Quick Sort
# Description: Implement quick sort algorithm
# Terminology:
#   - Divide and Conquer: Recursively divides problem into subproblems
#   - Pivot: Element used to partition the array
#   - Time Complexity: O(n log n) average, O(nÂ²) worst
# Algorithm Steps:
#   1. Choose pivot element
#   2. Partition array into elements < pivot and > pivot
#   3. Recursively sort subarrays
# Example:
#   Input: [10, 80, 30, 90, 40, 50, 70]
#   Process:
#     Pivot=70: [10, 30, 40, 50, 70, 80, 90]
#     Left partition (pivot=50): [10, 30, 40, 50]
#     Right partition (pivot=90): [80, 90]
#   Output: [10, 30, 40, 50, 70, 80, 90]
