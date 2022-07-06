
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = [[1,2,3], [4,5,6]]
matrix = [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ]


# Solution_1
row = len(matrix)
column = len(matrix[0])

temp = [[0] * row for _ in range(column)] # 행렬이 뒤바뀐 임시 행렬 필요
    
for i in range(row):  # 행 # 0,1
    for j in range(column):  # 열 # 0,1,2
        temp[j][row-1-i] = matrix[i][j]
        
print(temp)