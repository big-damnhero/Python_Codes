#https://practice.geeksforgeeks.org/problems/job-sequencing-problem/0

t = int(input())
for test in range(t):
    n = int(input())
    ar=list(map(int,input().split()))
    jobs = [[0,0,0] for i in range(n)]
    k=0
    i=0
    mx_dead = 0
    #print(jobs[0][0])
    while True:
        jobs[i][0]=ar[k]
        #print(jobs[i][0])
        k+=1
        jobs[i][1]=ar[k]
        k+=1
        mx_dead=max(mx_dead,jobs[i][1])
        jobs[i][2]=ar[k]
        i+=1
        k+=1
        if i==n:
            break
    jobs = sorted(jobs,key= lambda l:l[2],reverse=True)
    print(jobs)
    res = 0
    x=0
    vis = [False]*(n)
    for i in range(n):
        for j in range(min(n-1,jobs[i][1]-1),-1,-1):
            if vis[j]==False:
                res+=jobs[i][2]
                x+=1
                vis[j]=True
                break
    print(str(x)+" "+str(res))
