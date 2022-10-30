def LCS(x,y,n,m,t):
    if n==0 or m==0:
        return 0
    if t[n][m]!=-1:
        return t[n][m]
    if x[n-1] == y[m-1]:
        t[n][m]=1+LCS(x,y,n-1,m-1,t)
        return t[n][m]
    else:
        t[n][m]=max(LCS(x,y,n,m-1,t),LCS(x,y,n-1,m,t))
        return t[n][m]
if __name__ == "__main__":
    n=int(input())
    x=str(input())
    m=int(input())
    y=str(input())
    t=[[-1 for i in range(m+1)]for j in range(n+1)]
    print(LCS(x,y,n,m,t))
