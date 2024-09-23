#!/usr/bin/python3
""" 0. Change comes from within """

def makeChange(coins, total):
    """ Coin Change – Minimum Coins to Make total """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    miniCoinsNeeded = 0
    for coin in coins:
        if total / coin > 0:
            miniCoinsNeeded = miniCoinsNeeded + (total // coin)
            total = total % coin
        if not total:
            break

    if total != 0 or miniCoinsNeeded == 0:
        return -1
    return miniCoinsNeeded
