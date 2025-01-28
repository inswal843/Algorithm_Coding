import sys
input = sys.stdin.readline
N = int(input())
data = list(map(int, input().split()))
oper = list(map(int, input().split()))
max_val = -(sys.maxsize)
min_val = sys.maxsize
def back(value, step, opers):
    global max_val
    global min_val
    if step == N-1:
        max_val = max(max_val, value)
        min_val = min(min_val, value)
        return
    for i in range(4):
        if opers[i] != 0:
            if i==0:
                opers[i] = opers[i]-1
                back(value+data[step+1], step+1, opers)
                opers[i] = opers[i]+1
            elif i==1:
                opers[i] = opers[i]-1
                back(value-data[step+1], step+1, opers)
                opers[i] = opers[i]+1
            elif i==3:
                if value < 0:
                    opers[i] = opers[i]-1
                    back(-(abs(value)//data[step+1]), step+1, opers)
                    opers[i] = opers[i]+1
                else:
                    opers[i] = opers[i]-1
                    back(abs(value)//data[step+1], step+1, opers)
                    opers[i] = opers[i]+1
            else:
                opers[i] = opers[i]-1
                back(value*data[step+1], step+1, opers)
                opers[i] = opers[i]+1
back(data[0], 0, oper)
print(max_val)
print(min_val)