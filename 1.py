t = int(input())
res = 0
for _ in range(t):
    n, m = map(int, input().split())
    sum = 0
    i = 0
    while True:
        val = n + (1<<i)
        val = val//(1<<(i+1))
        if(val<=0):
            break
        val = (val*val)%m
        sum = (sum%m + val%m)%m
        i+= 1
    print(sum)