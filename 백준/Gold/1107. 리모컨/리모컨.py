import sys
input = sys.stdin.readline
tar = int(input())
T = int(input())
if T:
    broken = set(input().split())
else:
    broken = set()
min_count = abs(tar - 100)
for i in range(1000001):
    for word in str(i):
        if word in broken:
            break
    else:
        min_count = min(min_count, abs(tar - i) + len(str(i)))
print(min_count)