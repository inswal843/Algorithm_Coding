import sys
import heapq
input = sys.stdin.readline
n = int(input())
if n < 3:
    print(n)
    exit()
x = 1
y = 2
z = 3
for i in range(2, n-1):
    x, y = y, z
    z = (x+y) % 15746
print(z)