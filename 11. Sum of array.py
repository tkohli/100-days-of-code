# Sum of array
"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""


def runningSum(nums):
    sum = 0
    list = []
    for i in nums:
        sum = sum + i
        list.append(sum)
    return list

print(runningSum([[1,2,3,4]]))