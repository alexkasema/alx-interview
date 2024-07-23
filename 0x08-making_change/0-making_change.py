#!/usr/bin/python3
""" Change comes from within """


def makeChange(coins, total):
    """
    determine the fewest number of coins needed to meet a given amount total.
    """

    if total <= 0:
        return 0

    # Initialize an array with a value greater than any
    # possible number of coins needed
    num_coins = [float('inf')] * (total + 1)

    # Base case: 0 coins are needed to make the amount 0
    num_coins[0] = 0

    for i in range(total + 1):
        for coin in coins:
            if coin <= i:
                num_coins[i] = min(num_coins[i], num_coins[i - coin] + 1)

    return num_coins[total] if num_coins[total] != float('inf') else -1
