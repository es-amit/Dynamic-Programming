def LCS(x,y,n,m,t):
    if n==0 or m==0:
        return 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1]==y[j-1]:
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]= max(t[i][j-1],t[i-1][j])
    shortest_sequence=n+m-t[n][m]
    return shortest_sequence
if __name__ == "__main__":
    n = int(input())
    x = str(input())
    m = int(input())
    y = str(input())
    t=[[-1 for i in range(m+1)]for j in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                t[i][j]=0
    print(LCS(x,y,n,m,t))
