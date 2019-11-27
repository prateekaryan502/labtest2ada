A="saturday"
B="sunday"

result=[[None for i in range(len(B)+1)] for j in range(len(A)+1)]
print(result)
def minDistance( A, B):
    print(A,B)
    n = len(A)
    m = len(B)
    if result[n][m]!=None:
        return result[n][m]

    if n == 0:
        result[n][m]=m
        return m
    if m == 0:
        result[n][m]=n
        return n
    if A[n - 1] == B[m - 1]:
        result[n][m]=minDistance(A[:n-1], B[:m-1])
        return minDistance(A[:n-1], B[:m-1])

    result[n][m]=1 + min(minDistance(A, B[:m-1]), minDistance(A[:n-1], B), minDistance(A[:n-1], B[:m-1]))
    return (1 + min(minDistance(A, B[:m-1]), minDistance(A[:n-1], B), minDistance(A[:n-1], B[:m-1])))
# x=minDistance("geek","gesek")
# y=minDistance("cat","cut")
z=minDistance(A,B)
print(z)