import sys

input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    if sum(arr) == 0:
        break
    max_val = max(arr)
    total = 0
    for i in arr:
        if i != max_val:
            total += i**2
    print("right" if total == max_val**2 else "wrong")
