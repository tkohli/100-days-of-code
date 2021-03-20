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


# Effective solution
"""We make a hash table and then store sum that will lead to target sum then
   search for matching values in the array, we will get our result.
   Since, we are traversing array twice but not in a nested way, so we get
   less complexity"""


# O(n) Time Complexity / O(n) Space Complexity
def twoNumberSumEff(array, targetSum):
    nums = {}
    for num in array:
        if targetSum - num in nums:
            return [targetSum-num, num]
        else:
            nums[num] = True
    return []


# Effective solution
"""A very basic approach for array solving is sorting it, So
   we sort the array and then make 2 pointer(left and right)
   So we just perform a sum and get the desired output."""


# O(n log(n)) Time Complexity / O(1) Space Complexity
# O(n) Time Complexity / O(n) Space Complexity
def twoNumberSumSort(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        print(left, right)
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []


print(twoNumberSumNaive([3, 5, -4, 8, 11, 1, -1, 6], 10))
print(twoNumberSumEff([1, 2, 3], 5))
print(twoNumberSumSort([12, 3, 1, 2, -6, 5, -8, 6], 0))

