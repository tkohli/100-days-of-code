# 2 number sum
"""You are given an array of the distinct int & a target sum.
    We need to write a function to find 2 number which lead to target sum"""

# Naive Solution
"""Just using a nested loop and going to every element and checking the sum"""


# O(n^2) Time complexity / O(1) Space complexity
def twoNumberSumNaive(array, targetSum):
    for i in range(len(array)):
        firstNum = array[i]
        for j in range(i + 1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []


print(twoNumberSumNaive((3, 5, -4, 8, 11, 1, -1, 6), 10))
