import sys
input = sys.stdin.readline

from collections import Counter

x = int(input())
y = int(input())
z = int(input())

result = x*y*z

cnt = Counter(str(result))

for i in range(10):
    print(cnt[str(i)])