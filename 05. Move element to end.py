# Move element to end
""" We are given an array and an element, Write a function which takes all instances of element
    and moves it to the end. Make sure you don't use any extra space( other than variable),
    We can have any order in the starting all we need is same elements at the end"""
# ------------------------------------------------------------------------------------------------------------
""" Just take 2 pointers and swap the values when condition is met"""


# O(n) Time complexity / O(1) Space Complexity
def moveElementToEnd(array, toMove):
    i, j = 0, len(array) - 1
    while i < j:
        while array[j] == toMove:
            j -= 1
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i += 1
    return array
print(moveElementToEnd([1, 2, 4, 3, 2, 2, 2, 5], 2))


