# Product of Array Except Self
"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of
nums except nums[i].The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""




def productExceptSelf(nums):
    right_multiply = [0] * len(nums)
    right_multiply[-1] = nums[-1]
    for i in range(1, len(nums)):
        right_multiply[len(nums) - i - 1] = right_multiply[len(nums) - i] * nums[len(nums) - i - 1]
    output = [0] * len(nums)
    prefix = 1
    current_index = 0
    while current_index < len(output) - 1:
        output[current_index] = prefix * right_multiply[current_index + 1]
        prefix *= nums[current_index]
        current_index += 1
    output[-1] = prefix
    return output
    # result = []
    # x = 1
    # test = nums
    # if 0 in nums:
    #     for i in range(len(nums)):
    #         if nums[i] != 0:
    #             result.append(0)
    #         elif nums[i] == 0:
    #             test.remove(nums[i])
    #             result1 = (reduce(operator.mul, test))
    #             result.append(result1)
    #             nums.insert(i, 0)
    # else:
    #     for i in nums:
    #         result1 = (reduce(operator.mul, nums)) // i
    #         result1 = math.prod(nums)//i
    #         result.append(result1)
    # return result


# print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1, 1, 0, -3, 3]))
