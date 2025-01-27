import sys
from collections import deque
input = sys.stdin.readline
left = deque(input().strip())
right = deque()
T = int(input())
for _ in range(T):
    oper = list(map(str, input().split()))
    if oper[0] == "P":
        left.append(oper[1])
    elif oper[0] == "L":
        if left:
            right.appendleft(left.pop())
    elif oper[0] == "D":
        if right:
            left.append(right.popleft())
    else:
        if left:
            left.pop()
print("".join(left)+"".join(right))