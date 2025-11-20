import sys

input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == "0":
        break
    flag = True
    for i in range(len(s)//2):
        if s[i] != s[-(i+1)]:
            flag = False
            break
    print("yes" if flag else "no")