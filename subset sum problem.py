def knapsack(arr,sum,n,t):
    if n == 0 and sum == 0:
        return True
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if arr[i-1] <= j:
                t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j]=t[i-1][j]
    return t[n][sum]
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    sum = int(input())
    t=[[-1 for i in range(sum+1)] for j in range(n+1)]
    for i in range(0,n+1):
        for j in range(0,sum+1):
            if i == 0:
                t[i][j] = False
            if j == 0:
                t[i][j] = True
            else:
                continue
    ans = knapsack(arr,sum,n,t)
    if ans == True:
        print("YES")
    else:
        print("NO")

