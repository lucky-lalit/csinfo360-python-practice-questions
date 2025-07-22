# Exercise 4: Bidirectional Bubble Sort (Cocktail Shaker Sort)
# Description: Implement bidirectional bubble sort
# Terminology:
#   - Bidirectional: Sorting alternates between left-to-right and right-to-left
#   - Improvement: Can be more efficient than standard bubble sort
# Algorithm Steps:
#   1. Left-to-right pass (like bubble sort)
#   2. Right-to-left pass (bubbling smallest elements left)
#   3. Repeat until sorted
# Example:
#   Input: [5, 1, 4, 2, 8, 0, 2]
#   Process:
#     Forward Pass: [1, 4, 2, 5, 0, 2, 8]
#     Backward Pass: [0, 1, 4, 2, 2, 5, 8]
#     Forward Pass: [0, 1, 2, 4, 2, 5, 8]
#     Backward Pass: [0, 1, 2, 2, 4, 5, 8]
#   Output: [0, 1, 2, 2, 4, 5, 8]
