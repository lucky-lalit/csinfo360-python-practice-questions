# Exercise 5: Odd-Even Sort
# Description: Implement odd-even sort algorithm
# Terminology:
#   - Parallel Sort: Can be implemented to run in parallel
#   - Comparison Sort: Compares odd/even indexed pairs
# Algorithm Steps:
#   1. Compare all odd/even indexed pairs
#   2. Swap if out of order
#   3. Alternate between odd/even phases until sorted
# Example:
#   Input: [3, 2, 3, 8, 5, 6, 4, 1]
#   Process:
#     Odd Phase: [2, 3, 3, 8, 5, 6, 1, 4]
#     Even Phase: [2, 3, 3, 5, 8, 1, 6, 4]
#     Odd Phase: [2, 3, 3, 5, 1, 8, 4, 6]
#     Even Phase: [2, 3, 3, 1, 5, 4, 8, 6]
#     Odd Phase: [2, 1, 3, 3, 5, 4, 6, 8]
#     Even Phase: [1, 2, 3, 3, 4, 5, 6, 8]
#   Output: [1, 2, 3, 3, 4, 5, 6, 8]
