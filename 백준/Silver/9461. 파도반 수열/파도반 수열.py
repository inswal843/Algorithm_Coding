import sys
input = sys.stdin.readline
T = int(input())
padoban = [1] * 101
padoban[4], padoban[5] = 2, 2
for i in range(6, 101):
    padoban[i] = padoban[i-1] + padoban[i-5]
# print(padoban)
for _ in range(T):
    tar = int(input())
    print(padoban[tar])