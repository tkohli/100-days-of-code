# Number of Good Pairs
"""Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed
"""


def numIdenticalPairs(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    i, j = 0, 1
    while i in range(len(nums)):
        j = i + 1
        while j in range(len(nums)):
            # print(nums[i], nums[j])
            if nums[i] == nums[j]:
                count += 1
            j += 1
        i += 1
    return count
    # return sum([nums[i+1:].count(nums[i]) for i in range(len(nums))])


print(numIdenticalPairs([1, 2, 3, 1, 1, 3]))
print(numIdenticalPairs([1, 1, 1, 1]))
