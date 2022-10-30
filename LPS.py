def LPS(x,y,n,m,t):
    if n==0 or m==0:
        return 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1]==y[j-1]:
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i][j-1],t[i-1][j])
    return t[n][m]
if __name__ == "__main__":
    n=int(input())
    x=str(input())
    y=x[::-1]
    t=[[0 for i in range(n+1)]for j in range(n+1)]
    print(LPS(x,y,n,n,t))
