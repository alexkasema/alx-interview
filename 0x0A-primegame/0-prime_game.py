#!/usr/bin/python3
""" The Prime Game """


def isPrime(n):
    """ Check if a number is prime a prime number or not """
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


def calculate_primes(n, primes):
    """ Calculate all primes """
    top_prime = primes[-1]
    if n > top_prime:
        for i in range(top_prime + 1, n + 1):
            if isPrime(i):
                primes.append(i)
            else:
                primes.append(0)


def isWinner(x, nums):
    """
    x is the number of rounds and nums is an array of n.
    Return: name of the player that won the most rounds.
    If the winner cannot be determined, return None.
    You can assume n and x will not be larger than 10000.
    """

    scores = {"Maria": 0, "Ben": 0}

    primes = [0, 0, 2]

    calculate_primes(max(nums), primes)

    for round_num in range(x):
        sum_options = sum((i != 0 and i <= nums[round_num])
                          for i in primes[:nums[round_num] + 1])

        if (sum_options % 2):
            winner = "Maria"
        else:
            winner = "Ben"

        if winner:
            scores[winner] += 1

    if scores["Maria"] > scores["Ben"]:
        return "Maria"
    elif scores["Ben"] > scores["Maria"]:
        return "Ben"

    return None
