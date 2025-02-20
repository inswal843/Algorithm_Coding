import sys
input = sys.stdin.readline
data = [list(map(int, input().split())) for _ in range(9)]
data_T = list(map(list, zip(*data)))
empty_cells = [(i, j) for i in range(9) for j in range(9) if data[i][j] ==0]
def is_valid(x, y, num):
    if num in data[x]:
        return False
    elif num in data_T[y]:
        return False
    else:
        start_x, start_y = (x//3)*3, (y//3)*3
        for i in range(3):
            for j in range(3):
                if data[start_x+i][start_y+j]==num:
                    return False
    return True
def back(idx):
    if idx == len(empty_cells):
        for row in data:
            print(*row)
        sys.exit(0)
    else:
        x, y = empty_cells[idx]
        for i in range(1, 10):
            if is_valid(x, y, i):
                data[x][y] = i
                data_T[y][x] = i
                back(idx+1)
                data[x][y] = 0
                data_T[y][x] = 0
back(0)