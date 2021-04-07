# longest Peak
"""
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find length of peak how long it is. If the array contains multiple peaks, return the
longest peak available.


You may imagine that nums[-1] = nums[n] = -∞.
eg - Input: nums = [1,2,3,1]
Output: 4

"""

import math


# O(n) Time Complexity | O(1) Space Complexity
def longestPeak(array):
    longestPeakLength = 0
    i = 1
    while i < len(array)-1:
        isPeak = array[i-1] < array[i] and array[i] > array[i+1]
        if not isPeak:
            i += 1
            continue
        leftIdx = i - 2
        while leftIdx <= 0 and array[leftIdx] < array[leftIdx +1]:
            leftIdx -= 1
        rightIdx = i + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1
        currentLongestPeak = rightIdx - leftIdx - 1
        longestPeakLength = max(longestPeakLength,currentLongestPeak)
        i = rightIdx
    return longestPeakLength


print(longestPeak([1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]))
print(longestPeak([1,2,3,1]))