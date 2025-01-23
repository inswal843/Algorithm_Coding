import sys
import math
input = sys.stdin.readline
a, b, c = list(map(int, input().split()))
# print(a**b%c)
# remain = a%c
# for _ in range(b-1):
#     remain = remain * a % c
# print(remain)
# remain = [-1]
# for i in range(1, b):
#     if a%c in remain:
#         print(a%c, i)
#         break
#     else:
#         remain.append(a%c)
#         a = remain[i]*a
# print(remain)
def recpow(a, n, mod):
    # print(a, n)
    if n == 1:
        return a % mod
    elif n%2==0:
        result = recpow(a, n//2, mod)
        return (result * result) % mod
    else:
        result = recpow(a, (n-1)//2, mod)
        return (result * result * a) % mod
print(recpow(a, b, c))