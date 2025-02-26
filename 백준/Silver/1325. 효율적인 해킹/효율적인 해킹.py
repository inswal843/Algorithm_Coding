import sys
from collections import deque
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    e, s = map(int, input().split())
    graph[s].append(e)
# print(graph)
def bfs(start):
    q = deque()
    visited = [False] * (N+1)
    q.append(start)
    cnt = 0
    visited[start] = True
    for i in graph[start]:
        q.append(i)
    while q:
        node = q.popleft()
        if not visited[node]:
            cnt+=1
            visited[node] = True
            for i in graph[node]:
                q.append(i)
    return cnt
cnts = []
for i in range(1, N+1):
    cnts.append((bfs(i), i))
# print(cnts)
max_cnt, x = max(cnts)
# print(max_cnt)
for num, idx in cnts:
    if num == max_cnt:
        print(idx, end=" ")