import sys
def input(): return sys.stdin.readline().rstrip()

x = int(input())

d = [0]*(int(1e6)+1)

for i in range(2,x+1):
    d[i] = d[i-1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)

print(d[x])