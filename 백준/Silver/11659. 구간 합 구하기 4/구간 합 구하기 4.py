import sys
input = sys.stdin.readline
N, M = map(int, input().split())
data = list(map(int, input().split()))
# for _ in range(M):
#     i, j = map(int, input().split())
#     print(sum(data[i-1:j]))
# dp = [[0] for _ in range(N+1)]
# cnt = 0
# for i in range(1, N+1):
#     for j in range(1, N-i+2):
#         # print(i, j+cnt)
#         dp[i].append(dp[i][j-1]+data[j+cnt-1])
#     cnt+=1
# # print(dp)
# for _ in range(M):
#     i, j = map(int, input().split())
#     print(dp[i][j-i+1])
dp = [0] * (N+1)
for i in range(1, N+1):
    dp[i] = dp[i-1] + data[i-1]
# print(dp)
for _ in range(M):
    i, j = map(int, input().split())
    print(dp[j] - dp[i-1])