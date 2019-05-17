https://www.geeksforgeeks.org/greedy-algorithm-egyptian-fraction/

import math

t = int(input())
for test in range(t):
    nr,dr=map(int,input().split())
    ans = []
    while nr!=0:
        x = math.ceil(dr/nr)
        ans.append(x)
        nr = nr*x-dr
        dr = dr*x
    n = len(ans)
    for i in range(n):
        if i!=n-1:
            print("1/"+str(ans[i])+" + ",end="")
        else:
            print("1/"+str(ans[i]))
