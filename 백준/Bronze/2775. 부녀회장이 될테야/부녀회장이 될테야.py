import sys

input = sys.stdin.readline

T = int(input())

arr = [[0] * 15 for _ in range(16)]

arr[0] = [i for i in range(15)]

for i in range(1, 15):
    for j in range(1, 15):
        arr[i][j] = sum(arr[i-1][:j+1])
        
for _ in range(T):
    k = int(input())
    n = int(input())
    print(arr[k][n])
    
    