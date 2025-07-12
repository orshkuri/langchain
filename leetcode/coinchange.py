def coinchange(coins: list, amount: int) -> int:
    """ Minimal amount of coins to get to amount"""
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] = min(dp[a], dp[a - coin] + 1)
    return dp[amount] if dp[amount] != amount + 1 else -1


def coinchange_combinations(coins: list, amount: int) -> int:
    """ Minimal amount of coins to get to amount"""
    dp = [0] * (amount + 1)
    dp[0] = 1
    for a in range(1, amount + 1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] += (dp[a - coin])
    return dp[-1]

def coinchange_combinations_test(coins: list, amount: int) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for a in range(1, amount + 1):
            if a - coin >= 0:
                dp[a] += dp[a - coin]
    return dp[-1]


def coinchange_combinations_memory(coins: list, amount: int) -> int:
    dp = [[0] * (len(coins)) for _ in range(amount + 1)]  # amount * coins
    dp[0] = [1 for i in range(len(coins) + 1)]

    for a in range(1, amount + 1):
        for i in range(len(coins)):
            if a - coins[i] >= 0:  # use the coin i
                dp[a][i] = dp[a-coins[i]][i]
            if i > 0:  # dont use i
                dp[a][i] += dp[a][i-1]
    return dp[amount][len(coins) - 1]

# v = coinchange([1,5,6], 8)
# print(v)
v = coinchange_combinations_test([1,5,6, 2], 20)
print(v)

v = coinchange_combinations([1,5,6, 2], 20)
print(v)

v = coinchange_combinations_memory([1,5,6, 2], 20)
print(v)