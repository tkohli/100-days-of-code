# Subarray sort
"""
Given an array find sortest subarray whuch when sorted makes whole array sorted
eg = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
output = [3,9]
"""


def isOutOfOrder(i, num, array):
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]
    return num > array[i + 1] or num < array[i - 1]


def subarraySort(arr):
    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")
    for i in range(len(arr)):
        num = arr[i]
        if isOutOfOrder(i, num, arr):
            minOutOfOrder = min(minOutOfOrder, num)
            maxOutOfOrder = max(maxOutOfOrder, num)
    if minOutOfOrder == float("inf"):
        return [-1, -1]
    subarrayLeftIdx = 0
    while minOutOfOrder >= arr[subarrayLeftIdx]:
        subarrayLeftIdx += 1
    subarrayRightIdx = len(arr) - 1
    while maxOutOfOrder <= arr[subarrayRightIdx]:
        subarrayRightIdx -= 1
    return [subarrayLeftIdx, subarrayRightIdx]


print(subarraySort([1,2,3,10,4,2,3,5]))
# print(findLengthOfShortestSubarray([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
