import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = [list(map(str, input().strip())) for _ in range(n)]
nx = [0, 0, 1, -1]
ny = [1, -1, 0, 0]
cnt = 0
def dfs(path, x, y, step):
    global cnt
    cnt = max(cnt, step)
    for i in range(4):
        xx = x+nx[i]
        yy = y+ny[i]
        if 0 <= xx < n and 0 <= yy < m and data[xx][yy] not in path:
            path.add(data[xx][yy])
            dfs(path, xx, yy, step+1)
            path.remove(data[xx][yy])
path2 = set()
path2.add(data[0][0])
dfs(path2, 0, 0, 1)
print(cnt)