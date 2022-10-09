def knapsack(arr,n,sum):
    if n==0 or sum==0:
        return True
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if arr[i-1]<=j:
                t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
            else:
                t[i][j]=t[i-1][j]
    return t[n][sum]
if __name__ == "__main__":
    n=5
    #arr=[1,5,11,5]
    arr=[1,2,3,4,5]
    if sum(arr) % 2!=0:
        print("NO")
    else:
        t=[[-1 for i in range(sum(arr)+1)]for j in range(n+1)]
        for i in range(n+1):
            for j in range(sum(arr)+1):
                if i == 0:
                    t[i][j]=False
                if j==0:
                    t[i][j]=True

        ans=knapsack(arr,n,sum(arr)//2)
        if ans == True:
            print("YES")
        else:
            print("NO")
