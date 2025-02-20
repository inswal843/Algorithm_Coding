import sys
import heapq
input = sys.stdin.readline
N = int(input())
M = int(input())
data = [[] for _ in range(N)]
for _ in range(M):
    s, e, c = list(map(int, input().split()))
    data[s-1].append((e-1, c))
costs = [sys.maxsize] * N
S, E = map(int, input().split())
S-=1
E-=1
q = []
costs[S] = 0
heapq.heappush(q, (0, S))
while q:
    cost, node = heapq.heappop(q)
    if costs[node] < cost:
        continue
    for e, c in data[node]:
        new_cost = cost+c
        if costs[e] > new_cost:
            costs[e] = new_cost
            heapq.heappush(q, (costs[e], e))
print(costs[E])