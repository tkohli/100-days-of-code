"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.
"""


# O(n) Time Complexity | O(1) Space Complexity
def isMonotonic(A):
    x = True
    y = True
    for i in range(1, len(A)):
        if A[i] < A[i - 1]:
            x = False
        if A[i] > A[i - 1]:
            y = False

    return x or y