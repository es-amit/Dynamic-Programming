def knapsack(wt,val,w,n,t):
    if n==0 or w==0:
        return 0
    for i in range(1,n+1):
        for j in range(1,w+1):
            if wt[i-1] <= j:
                t[i][j] = max(val[i-1]+t[i-1][j-wt[i-1]],t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[n][w]
if __name__ == '__main__':
    n=int(input())
    wt=list(map(int,input().split()))
    val=list(map(int,input().split()))
    w=int(input())
    t = [[-1 for i in range(w + 1)] for j in range(n + 1)]
    for i in range(n+1):
        for j in range(w+1):
            if i == 0 or j == 0:
                t[i][j] = 0
    print(knapsack(wt,val,w,n,t))
