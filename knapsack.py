values=[60,100,120]
weights=[10,20,30]
capacity=50
n=len(weights)
result=[[None for i in range(n+1)]for j in range(capacity+1)]
def knapsack(w,v,c,n):
    if result[c][n]!=None:
        return result[c][n]
    if n==0 or c<=0:
        result[c][n]=0
        return 0
    if w[n-1]>c:
        result[c][n]=knapsack(w,v,c,n-1)
        return knapsack(w,v,c,n-1)
    else:
        result[c][n]=max(v[n-1]+knapsack(w,v,c-w[n-1],n-1),knapsack(w,v,c,n-1))
        return max(v[n-1]+knapsack(w,v,c-w[n-1],n-1),knapsack(w,v,c,n-1))


print(knapsack(weights,values,capacity,n))