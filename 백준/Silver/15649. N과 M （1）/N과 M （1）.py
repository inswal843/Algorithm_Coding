import sys
input = sys.stdin.readline
N, M = map(int, input().split())
data = [i for i in range(1, N+1)]
# print(data)
def dfs(path, step):
    if step == M:
        print(" ".join(map(str, path)))
        return
    else:
        for i in range(N):
            if data[i] not in path:
                path.append(data[i])
                dfs(path, step+1)
                path.pop()
dfs([], 0)