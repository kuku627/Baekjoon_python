grid = []
for _ in range(9):
    row = list(map(int, input().split()))
    grid.append(row)

max_value = -1
row_index, col_index = -1, -1


for i in range(9):
    for j in range(9):
        if grid[i][j] > max_value:
            max_value = grid[i][j]
            row_index = i + 1  
            col_index = j + 1  


print(max_value)
print(row_index, col_index)