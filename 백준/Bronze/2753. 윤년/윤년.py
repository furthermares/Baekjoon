import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())
if((N%4==0 and not N%100==0) or N%400==0): print(1)
else: print(0)