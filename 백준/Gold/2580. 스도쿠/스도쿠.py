import sys
input = sys.stdin.readline
data = [list(map(int, input().split())) for _ in range(9)]
data_tran = list(map(list, zip(*data)))
empty = []
for i in range(9):
    for j in range(9):
        if data[i][j] == 0:
            empty.append((i, j))
# print(empty)
def is_vaild(x, y, num):
    global data, data_tran
    if num in data[x] or num in data_tran[y]:
        return False
    x_start = x//3 * 3
    y_start = y//3 * 3
    for i in range(3):
        for j in range(3):
            if data[x_start+i][y_start+j] == num:
                return False
    return True
def back(cnt):
    if cnt == len(empty):
        for i in range(9):
            print(*data[i])
        exit(0)
    else:
        x, y = empty[cnt]
        for i in range(1, 10):
            if is_vaild(x, y, i):
                data[x][y] = i
                data_tran[y][x] = i
                back(cnt+1)
                data[x][y] = 0
                data_tran[y][x] = 0
back(0)