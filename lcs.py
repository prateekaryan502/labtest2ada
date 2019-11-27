
a="AGGTAB"
b="GXTXAYB"
result=[[None for i in range(len(b)+1)] for j in range(len(a)+1)]

def lcs(a,b):
    n=len(a)
    m=len(b)
    if result[n][m]!=None:
        return result[n][m]
    else:
        if n==0 or m==0:
            result[n][m]=0
            return 0
        if a[n-1]==b[m-1]:
            result[n][m]=1+lcs(a[:n-1],b[:m-1])
            print(a[n-1],end="")
            return 1+lcs(a[:n-1],b[:m-1])
        else:
            result[n][m]=max(lcs(a[:n-1],b),lcs(a,b[:m-1]))
            return max(lcs(a[:n-1],b),lcs(a,b[:m-1]))

print()
x=lcs(a,b)
print()
print(x)