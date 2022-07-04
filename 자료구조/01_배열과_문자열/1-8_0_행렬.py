
# Solution_1
m, n = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(m)] 

for i in range(m):      # 행
    for j in range(n):  # 열
        if matrix[i][j] == 0:
            row = i
            column = j

for i in range(m):     # 원소가 속한 열
    matrix[i][column] = 0

for j in range(len(n):  # 원소가 속한 행
    matrix[row][j] = 0
