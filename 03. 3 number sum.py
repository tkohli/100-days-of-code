# 3 Number sum
""" Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
    The function should find all triplets in the array that sum up to the target sum and return a two-dimensional
    array of all these triplets. The numbers in each triplet should be ordered in ascending order, and the
    triplets themselves should be ordered in ascending order with respect to the numbers they hold.
    If no three numbers sum up to the target sum, the function should return an empty array."""
# ------------------------------------------------------------------------------------------------------------
""" We can make just a normal program with the 3 loops so that will be very inefficient program.
    So, we can make a hash table again but it will increase the complexity. What we can do is fix a point
    and then traverse the array with left and right pointer, that it is pretty easy to solve.
    Cs = Cn + L + R
    if Cs < targetSum <-- move left pointer to right
    if Cs > targetSum <-- move right pointer to left
    if Cs = targetSum <-- move both pointers at the same time """


# O(n^2) Time complexity / O(1) Space Complexity
def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):         # len(array)-1 so that we always have 2 elements left to find a triplet
        left = i+1
        right = len(array) - 1
        while left < right:
            
            currSum = array[i] + array[left] + array[right]
            if currSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currSum < targetSum:
                left += 1
            elif currSum > targetSum:
                right -= 1
    return triplets


print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))


