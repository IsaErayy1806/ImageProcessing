#%% Zİgzag conversion
""" 
Zigzag Conversion
"""
def convert(s, numRows, column):
    if numRows == 1 or numRows >= len(s):
        return s

    grid = [['' for _ in range(column)] for _ in range(numRows)]
    direction_down = False
    row, col = 0, 0

    for char in s:
        grid[row][col] = char
        if row == 0 or row == numRows - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1
        col += 1

    result = ''.join([''.join(row) for row in grid])
    return result

input_str = "PAYPALISHIRING"
numRows = 3
column = len(input_str)  # You can calculate the number of columns dynamically
result = convert(input_str, numRows, column)
print(result)  # Output: "PAHNAPLSIIGYIR"