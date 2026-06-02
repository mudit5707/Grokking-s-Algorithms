def LeastNumberOfCoins(coins, target):
    dp = [float("inf")]*(target+1)
    dp[0] = 0
    for i in range(1, target+1):
        for coin in coins[::-1]:
            if coin <= i:
                if dp[i-coin] == float("inf") : continue
                dp[i] = min(1 + dp[i - coin], dp[i])
    return dp[target]

coins = [1, 4, 5, 6]
target = 8
print(LeastNumberOfCoins(coins, target))