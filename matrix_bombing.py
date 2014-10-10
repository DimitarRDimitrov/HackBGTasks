def matrix_bombing(m):
    dictionary = {}
    for line in m:
        for row in line:
            dictionary.update({line: row})
    bomb_location = raw_input("Coordinates of the bomb:")
    total = sum(dictionary)

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix_bombing(m))