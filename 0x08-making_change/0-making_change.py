#!/usr/bin/python3
""" 0. Change comes from within """
import sys


def makeChangeUtil(coins, length, total, dp):
    """ Utility function for solving the minimum coins problem """
    # Base case: If target value total is 0, no coins are needed
    if total == 0:
        return 0

    # If subproblem is already solved, return the result from DP table
    if dp[total] != -1:
        return dp[total]

    ans = sys.maxsize

    # Iterate over all coins and recursively solve for subproblems
    for i in range(length):
        if coins[i] <= total:
            # Recursive call to solve for remaining value total - coins[i]
            res = makeChangeUtil(coins, length, total - coins[i], dp)

            if res != sys.maxsize and res + 1 < ans:
                ans = res + 1

    # Save the result in the DP table
    dp[total] = ans

    return ans


def makeChange(coins, total):
    """ Coin Change – Minimum Coins to Make total """
    if total == 0:
        return 0
    dp = [-1] * (sum + 1)
    coins_size = len(coins)
    ans = makeChangeUtil(coins, coins_size, total, dp)
    if ans == sys.maxsize:
        return -1
    return ans
