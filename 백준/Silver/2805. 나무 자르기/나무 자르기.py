import sys
input = sys.stdin.read
data = input().split()

N, M = int(data[0]), int(data[1])
woods = list(map(int, data[2:]))

start, end = 1, max(woods)

while start <= end:
    mid = (start + end) // 2
    # wood_sum 계산 최적화
    wood_sum = sum(max(wood - mid, 0) for wood in woods)

    if wood_sum >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
