import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
t, p = map(int, input().split())

t_num = 0

for num in arr:
    if num%t == 0:
        t_num += num//t
    else:
        t_num += num//t + 1
print(t_num)
tot = sum(arr)
print(tot//p, tot%p, sep=" ")