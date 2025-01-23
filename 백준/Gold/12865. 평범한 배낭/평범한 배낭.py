import sys
input = sys.stdin.readline
n, k = map(int, input().split())
dp = [[0]*(k+1) for _ in range(n+1)]
items = [(0, 0)]
for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v))
# print(items)
for i in range(1, n+1):
    for j in range(1, k+1):
        if j < items[i][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], items[i][1]+dp[i-1][j-items[i][0]])
print(dp[n][k])