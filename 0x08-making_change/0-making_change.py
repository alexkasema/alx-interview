#!/usr/bin/python3
""" Change comes from within """


def makeChange(coins, total):
    """
    determine the fewest number of coins needed to meet a given amount total.
    """

    if total <= 0:
        return 0

    tmp = total

    num_coins_count = 0
    coin_idx = 0

    sorted_coins = sorted(coins, reverse=True)

    coins_len = len(coins)

    while tmp > 0:
        if coin_idx >= coins_len:
            return -1

        if tmp - sorted_coins[coin_idx] >= 0:
            tmp -= sorted_coins[coin_idx]
            num_coins_count += 1
        else:
            coin_idx += 1

    return num_coins_count
