# ZigZag traversal
def zigzagTraversal(arr):
    out = []
    test = 1
    # for i in range(len(arr)):
    #     for j in range(len(arr[0])):
    #         print(i+ j, end=" ")
    #     print("")
    # print("-----------------")
    out.append(arr[0][0])
    while test <= len(arr)+len(arr[0]):
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


print(zigzagTraversal([[1, 3, 4, 10],
                       [2, 5, 9, 11],
                       [6, 8, 12, 15],
                       [7, 13, 14, 16]]))
