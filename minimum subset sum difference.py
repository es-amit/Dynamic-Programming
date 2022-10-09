def knapsack(arr,sum,n,t):
    if n == 0 or sum == 0:
        return 0
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if arr[i-1]<=j:
                t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j]=t[i-1][j]

    return t

def min_sum_diff(sum,t):
    min_diff = sum
    for i in range((sum + 1)//2):
        if t[n][i] != False:
            equation = sum - 2 * i
            if min_diff > equation:
                min_diff = equation
    return min_diff
if __name__ =="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    sum=sum(arr)
    t=[[-1 for i in range(sum+1)]for j in range(n+1)]
    for i in range(n+1):
        for j in range(sum+1):
            if i==0:
                t[i][j]=False
            if j == 0:
                t[i][j]=True

    subset_sum=knapsack(arr,sum,n,t)
    print(min_sum_diff(sum,t))
