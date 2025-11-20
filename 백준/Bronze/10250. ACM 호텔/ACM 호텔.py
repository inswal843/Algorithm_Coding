import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    if n % h == 0:
        lev = str(h)
        room = str(n // h)
    else:
        lev = str(n - h * (n//h))
        room = str(n // h + 1)
    print(lev + room if len(room) == 2 else lev + "0" + room)