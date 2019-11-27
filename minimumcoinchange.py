coins = [9, 6, 5, 1]
m = len(coins)
V = 11
result=[None for i in range(V+1)]
import sys
def minCoins(coins, m, V):
    if result[V]!=None:
        return result[V]
    if (V == 0):
        return 0

    res = sys.maxsize
    for i in range(0, m):
        if (coins[i] <= V):
            sub_res = minCoins(coins, m, V - coins[i])
            if (sub_res != sys.maxsize and sub_res + 1 < res):
                res = sub_res + 1
    result[V]=res
    return res


print("Minimum coins required is", minCoins(coins, m, V))


