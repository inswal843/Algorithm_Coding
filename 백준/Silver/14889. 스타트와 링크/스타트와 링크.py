import sys
input = sys.stdin.readline
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
min_val = sys.maxsize
def back(n, idx):
    global min_val
    global visited
    if n == N//2:
        team1 = 0
        team2 = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    team1 += data[i][j]
                elif not visited[i] and not visited[j]:
                    team2 += data[i][j]
        min_val = min(min_val, abs(team1 - team2))
    else:
        for i in range(idx, N):
            visited[i] = True
            back(n+1, i+1)
            visited[i] = False
back(0, 0)
print(min_val)