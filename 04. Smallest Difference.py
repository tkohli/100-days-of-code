# Smallest Difference
from numpy import inf
""" We are given 2 arrays, we have to find 2 number such that their difference is smallest."""
# ------------------------------------------------------------------------------------------------------------
""" We can do 2 for loops but it will be naive solution, to do it effectively we sort the 
    arrays and then loop through them one to find out smallest sum"""


# O(n log(n) + m log(m)) Time complexity / O(1) Space Complexity
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne, idxTwo = 0, 0
    current = float(inf)
    smallest = float(inf)
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        if firstNum ==  secondNum:
            return [firstNum, secondNum]
        elif firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        else:
            current = firstNum - secondNum
            idxTwo += 1
        if smallest > current:
            smallest = current
            smallestPair = [firstNum, secondNum]
    return smallestPair


print(smallestDifference([-1, 5, 10, 20, 28, 3], [15, 17, 26, 135, 134]))


