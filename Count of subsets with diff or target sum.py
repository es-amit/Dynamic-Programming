def knapsack(arr,sum,n,t):
    if n == 0 or sum == 0:
        return 0
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if arr[i-1]<=j:
                t[i][j]=t[i-1][j-arr[i-1]]+t[i-1][j]
            else:
                t[i][j]=t[i-1][j]
    return t[n][sum]
if __name__ == "__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    diff=int(input())
    sum=sum(arr)
    t=[[-1 for i in range(sum+1)]for j in range(n+1)]
    for i in range(n+1):
        for j in range(sum+1):
            if i==0:
                t[i][j]=0
            if j == 0:
                t[i][j]=1

    sum_p1=(diff+sum)//2
    print(knapsack(arr,sum_p1,n,t))
