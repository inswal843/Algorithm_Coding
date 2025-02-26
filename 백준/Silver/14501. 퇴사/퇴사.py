import sys
input = sys.stdin.readline
N = int(input())
jobs = []
for i in range(N):
    day, gold = map(int, input().split())
    jobs.append((day, gold))
dp = [0] * (N+1)
for i in range(N-1, -1, -1):
    day, gold = jobs[i]
    if i + day > N:
        dp[i] = dp[i+1]
    else:
         dp[i] = max(dp[i+1], dp[i+day]+gold)
print(dp[0])