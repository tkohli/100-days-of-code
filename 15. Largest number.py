# Largest number
"""
Given a list of non-negative integers nums, arrange them such that they form the largest number.
Note: The result may be very large, so you need to return a string instead of an integer.
Input: nums = [3,30,34,5,9]
Output: "9534330"
"""


def largestNumber(nums):
    ans = []
    while nums != []:
        maxDigit = 0
        for num in nums:
            if greaterOrEqual(num, maxDigit):
                maxDigit = num
        ans.append(maxDigit)
        nums.remove(maxDigit)
    return ans


def greaterOrEqual(digit, max_digit):
    return int(str(digit) + str(max_digit)) >= int(str(max_digit) + str(digit))


print(largestNumber([10, 2]))
print(largestNumber([3, 30, 34, 5, 9]))
