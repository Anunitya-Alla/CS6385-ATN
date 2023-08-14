ID = "2021615994"
digits = [int(d) for d in ID]

bitS = [0 if d%2 ==0 else 1 for d in digits]
extBS = bitS * 68

n = 26 
adjM = [[0 for i in range(n)] for i in range(n)]

for i in range(n):
    for j in range(0,n):
        adjM[i][j] = extBS.pop(0)


degree = [sum(adjM[i]) for i in range(n)]
print(degree)

for i in range(n):
    adjM[i][i] = 0



for i in range(n):
    for j in range(i+1,n):
        adjM[j][i] = adjM[i][j]




print(adjM)









def is_symmetric(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    if rows != cols:
        return False

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                return False

    return True

# Example matrix
matrix = [
    [0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
    # Rest of the matrix elements...
]

if is_symmetric(adjM):
    print("The matrix is symmetric.")
else:
    print("The matrix is not symmetric.")


print(adjM[25])