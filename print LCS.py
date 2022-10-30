def LCS(x,y,n,m,t):
    if n==0 or m==0:
        return 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1]==y[j-1]:
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    return t

def print_LCS(x,y,n,m,t):
    i,j=n,m
    s=str()
    while i>0 and j>0:
        if x[i-1] == y[j-1]:
            s+=x[i-1]
            i-=1
            j-=1
        else:
            if t[i-1][j] > t[i][j-1]:
                i-=1
            else:
                j-=1
    return s[::-1]

if __name__ == '__main__':
    n=int(input())
    x=str(input())
    m=int(input())
    y=str(input())
    t=[[0 for i in range(m+1)]for j in range(n+1)]
    LCS(x,y,n,m,t)
    print(print_LCS(x,y,n,m,t))