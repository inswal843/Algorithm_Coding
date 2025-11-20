import sys

input = sys.stdin.readline

n = int(input())
s = input().rstrip()

r = 31
m = 1234567891

total = 0

for i in range(len(s)):
    total += (ord(s[i])-96) * r**i
    
print(total%m)