# Largest range
"""
We are given an array find the largest range it contains, range means number of consecutive numbers
eg - [1,11,3,0,5,2,4,10,7,12,6]
o/p- [0,7]
"""


def largestRangeNaive(nums):
    longestLength = 0
    nums.sort()
    count = 0
    for i in range(len(nums)-1):
        # print(nums[i]==nums[i+1]-1)
        if nums[i]==nums[i + 1]-1:
            count += 1
        else:
            count = 0
        longestLength = max(longestLength, count)
    return longestLength


def largestNumber(arr):
    bestRange = []
    longestLength = 0
    nums = {}
    for num in arr:
        nums[num] = True
    for num in arr:
        if not nums[num]:
            continue
        nums[num] = False
        currentLength = 1
        left = num-1
        right = num +1
        while left in nums:
            nums[left] = False
            currentLength+=1
            left -=1
        while right in nums:
            nums[right] =False
            currentLength+=1
            right+=1
        if currentLength > longestLength:
            longestLength = currentLength
            bestRange = [left+1,right-1]
    return bestRange


# print(largestRangeNaive([1,11,3,0,5,2,4,10,7,12,6]))
print(largestNumber([1,11,3,0,5,2,4,10,7,12,6]))