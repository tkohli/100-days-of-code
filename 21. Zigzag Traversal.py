# ZigZag traversal
# O(n^2) Time complexity | O(n) Space complexity
def zigzagTraversalNaive(arr):
    out = []
    test = 1
    # for i in range(len(arr)):
    #     for j in range(len(arr[0])):
    #         print(i+ j, end=" ")
    #     print("")
    # print("-----------------")
    out.append(arr[0][0])
    while test <= len(arr) + len(arr[0]):
        for j in range(len(arr[0])):
            for i in range(len(arr)):
                if test % 2 == 1:
                    if i + j == test:
                        # print(arr[i][j])
                        out.append(arr[i][j])
                else:
                    if i + j == test:
                        out.append(arr[j][i])
        test += 1
    return out


# O(n) Time complexity | O(n) Space complexity
def zigzagTraversal(arr):
    height = len(arr) - 1
    width = len(arr[0]) - 1
    result = []
    row, col = 0, 0
    going_down = True
    while not isOutOfBounds(row, col, height, width):
        result.append(arr[row][col])
        if going_down:
            if col == 0 or row == height:
                going_down = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row == 0 or col == width:
                going_down = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1
    return result


def isOutOfBounds(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width


print(zigzagTraversal([[1, 3, 4, 10],
                       [2, 5, 9, 11],
                       [6, 8, 12, 15],
                       [7, 13, 14, 16]]))
print(zigzagTraversalNaive([[1, 3, 4, 10],
                            [2, 5, 9, 11],
                            [6, 8, 12, 15],
                            [7, 13, 14, 16]]))
