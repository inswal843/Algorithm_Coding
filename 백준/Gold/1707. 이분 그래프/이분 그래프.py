import sys
from collections import deque
input = sys.stdin.readline
def bfs(start):
    q = deque()
    q.append(start)
    global colored
    global doomed
    colored[start] = 1
    while q:
        # print(q)
        node = q.popleft()
        # print(graph)
        for i in graph[node]:
            # print(i)
            if colored[i] == 0:
                colored[i] = colored[node]%2+1
                q.append(i)
            elif colored[i] == colored[node]:
                doomed = True
                return
    # colored[0] = 1
    # print(colored)
    # print("YES" if 0 not in colored else "NO")
K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    colored = [0] * (V+1)
    doomed = False
    for i in range(1, V+1):
        if colored[i] == 0:
            bfs(i)
        # print(i, doomed)
        if doomed:
            print("NO")
            break
    if not doomed:
        print("YES")