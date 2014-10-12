def matrix_bombing(m):
    for row in range(len(m)):
        for col in range(len(m[0])):
            print(m[row][col])
            if len(m) < row > 0 and len(m[0]) > col > 0:
                m[row-1][col-1] -= m[row][col]
                m[row-1][col] -= m[row][col]
                m[row-1][col+1] -= m[row][col]
                m[row][col-1] -= m[row][col]
                m[row][col+1] -= m[row][col]
                m[row+1][col-1] -= m[row][col]
                m[row+1][col] -= m[row][col]
                m[row+1][col+1] -= m[row][col]
                for i in m:
                    if i < 0:
                        i = 0
                print(sum(m))
                # mneeeeeeeeeeeeeeeee

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix_bombing(m))
