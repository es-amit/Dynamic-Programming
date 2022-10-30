def LPS(x,y,n,m,t):
    if n==0 or m==0:
        return 0
    no_of_deletion=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1]==y[j-1]:
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i][j-1],t[i-1][j])
    no_of_deletion=n-t[n][m]
    return no_of_deletion
if __name__ == "__main__":
    n=int(input())
    x=str(input())
    y=x[::-1]
    t=[[0 for i in range(n+1)]for j in range(n+1)]
    print(LPS(x,y,n,n,t))
