import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
Q = deque([n])
visited = [-1] * 100001
visited[n] = 0
while Q:
    cur = Q.popleft()
    if cur == k:
        print(visited[cur])
        break
    for i in (cur*2, cur-1, cur+1):
        if 0<= i < 100001 and visited[i] == -1:
            if i == cur*2:
                visited[i] = visited[cur]
            else:
                visited[i] = visited[cur] + 1
            Q.append(i)