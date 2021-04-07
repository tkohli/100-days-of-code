# highest Peak
"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks,
return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.
eg - Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
"""

import math
# O(n) Time Complexity | O(1) Space Complexity
def findPeakElement(nums):
    peaksIndex = float('-inf')
    val = 0

    if len(nums) == 1:
        return 0
    for i in range(0, len(nums) - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            test = nums[i]
            if test > val:
                peaksIndex = i

    if peaksIndex == float('-inf'):
        if nums[0] < nums[1]:
            return len(nums) - 1
        else:
            return 0
    return peaksIndex


print(findPeakElement([1,2]))
print(findPeakElement([4,3,2,1]))
print(findPeakElement([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
