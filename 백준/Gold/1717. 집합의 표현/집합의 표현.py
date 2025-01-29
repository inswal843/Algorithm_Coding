import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
# print(parent)
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x] 
def union_parent(a, b):
    x, y = find_parent(a), find_parent(b)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
for _ in range(m):
    op, x, y = list(map(int, input().split()))
    if op == 1:
        if find_parent(x) == find_parent(y):
            print("YES")
        else:
            print("NO")
    else:
        union_parent(x, y)