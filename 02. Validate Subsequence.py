# Validate Subsequence
""" We are given 2 array we have to find that is it a subsequence or not
    eg: [5, 1, 22, 25, -1, 8, 10], [1, 6,-1,10]
    we can delete some integers and then we should have subsequence.
    It has to be in the same sequence."""


# O(n) Time Complexity / O(1) Space Complexity
def valSubsequence(array, sequence):
    arrIdx, seqIdx = 0, 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)


print(valSubsequence([5, 1, 22, 6, 25, -1, 8, 10], [1, 6,-1,10]))