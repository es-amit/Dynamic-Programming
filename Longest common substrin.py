def LCS(x,y,n,m,t):
    best_count=0
    if n==0 or m==0:
        return 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1]==y[j-1]:
                t[i][j]=1+t[i-1][j-1]
                best_count=max(t[i][j],best_count)
            else:
                t[i][j]=0
    return best_count
if __name__ == "__main__":
    n = int(input())
    x = str(input())
    m = int(input())
    y = str(input())
    t = [[-1 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
    print(LCS(x,y,n,m,t))
