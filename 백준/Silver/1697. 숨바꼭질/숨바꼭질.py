import sys
from collections import deque
sys.setrecursionlimit(100000)
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
    for next_pos in (cur+1, cur-1, cur*2):
        if -1 < next_pos <= 100000 and visited[next_pos] == -1:
            visited[next_pos] = visited[cur]+1
            Q.append(next_pos)