# Spiral traversal
"""
Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""


# O(n) Time Complexity | O(n) Space Complexity
def spiralTraversal(matrix):
    result = []
    sR, eR = 0, len(matrix) - 1
    sC, eC = 0, len(matrix[0]) - 1
    # print(matrix[sR][eR])

    while sR <= eR and sC <= eC:
        for col in range(sC, eC + 1):
            print(matrix[sR][col], 4,sR,col)
            result.append(matrix[sR][col])

        for row in range(sR + 1, eR + 1):
            print(matrix[row][eC], 3)
            result.append(matrix[row][eC])

        for col in reversed(range(sC, eC)):
            if sR == eR:
                break
            print(matrix[eR][col], 2,eR,col)
            result.append(matrix[eR][col])

        for row in reversed(range(sR + 1, eR)):
            if sC == eC:
                break
            print(matrix[row][sC], 1)
            result.append(matrix[row][sC])

        sR += 1
        sC += 1
        eR -= 1
        eC -= 1
    return result

print(spiralTraversal([[7],[9],[6]]))
# print(spiralTraversal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5])
# print(spiralTraversal([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
