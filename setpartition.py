arr = [1,5,11,5]
n = len(arr)
sum=sum(arr)
result=[[None for i in range(sum+1)] for i in range(n+1)]
def isSubsetSum(arr, n, sum):
    if result[n][sum]!=None:
        return result[n][sum]
    if sum == 0:
        result[n][sum]=True
        return True
    if n == 0 and sum != 0:
        result[n][sum]=False
        return False
    if arr[n - 1] > sum:
        result[n][sum]=isSubsetSum(arr, n - 1, sum)
        return isSubsetSum(arr, n - 1, sum)
    result[n][sum]=isSubsetSum(arr, n - 1, sum) or isSubsetSum(arr, n - 1, sum - arr[n - 1])
    return isSubsetSum(arr, n - 1, sum) or isSubsetSum(arr, n - 1, sum - arr[n - 1])

def findPartion(arr, n):
    sum = 0
    for i in range(0, n):
        sum += arr[i]

    if sum % 2 != 0:
        return false
    return isSubsetSum(arr, n, sum // 2)


arr = [1,5,11,5]
n = len(arr)
if findPartion(arr, n) == True:
    print("Can be divided into two subsets of equal sum")
else:
    print("Can not be divided into two subsets of equal sum")
