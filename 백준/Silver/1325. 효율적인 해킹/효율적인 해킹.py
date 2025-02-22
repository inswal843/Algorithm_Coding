import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    e, s = map(int, input().split())
    graph[s].append(e)
def bfs(start):
    q = deque()
    visited = [False] * (N+1)
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
answers = []
for i in range(1, N+1):
    answers.append((bfs(i), i))
# print(answers)
max_cnt, x = max(answers)
ans = []
for i in range(N):
    a, b = answers[i]
    if a == max_cnt:
        ans.append(b)
ans.sort()
print(*ans)