#!/usr/bin/python3
"""
Maria and Ben are playing a game. Given a set of consecutive integers
starting from 1 up to and including n, they take turns choosing a prime
number from the set and removing that number and its multiples from the set.
The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally, determine
who the winner of each game is.

Prototype: def isWinner(x, nums)
where x is the number of rounds and nums is an array of n
Return: name of the player that won the most rounds
If the winner cannot be determined, return None
You can assume n and x will not be larger than 10000
You cannot import any packages in this task
Example:

x = 3, nums = [4, 5, 1]
First round: 4

Maria picks 2 and removes 2, 4, leaving 1, 3
Ben picks 3 and removes 3, leaving 1
Ben wins because there are no prime numbers left for Maria to choose
Second round: 5

Maria picks 2 and removes 2, 4, leaving 1, 3, 5
Ben picks 3 and removes 3, leaving 1, 5
Maria picks 5 and removes 5, leaving 1
Maria wins because there are no prime numbers left for Ben to choose
Third round: 1

Ben wins because there are no prime numbers for Maria to choose
Result: Ben has the most wins
"""


def isWinner(x, nums):
    """
    Determine the winner of a prime number game played for x rounds with
    different sets of numbers.

    Parameters:
    - x (int): The number of rounds to play
    - nums (list): An array of integers representing the upper limits
    for each round

    Returns:
    - str: The name of the player who won the most rounds. If the winner
    cannot be determined, return None
    """
    if not x or x < 1 or not nums or not len(nums):
        return None

    player_wins = {
        "Maria": 0,
        "Ben": 0,
    }
    # iterate through the round x
    for round in range(x):
        size_of_primes = len(get_prime_numbers(nums[round]))
        if size_of_primes % 2 == 0:
            player_wins["Ben"] += 1
        else:
            player_wins["Maria"] += 1
    players = sorted(player_wins.keys())
    if player_wins[players[0]] > player_wins[players[1]]:
        return players[0]
    return players[1]


def get_prime_numbers(n):
    """
    Generate a list of prime numbers up to a given integer n using the
    Sieve of Eratosthenes algorithm.

    Parameters:
    - n (int): The upper limit integer up to which to find prime numbers

    Returns:
    - list: A list of prime numbers from 2 up to n
    """
    set_numbers = [True for i in range(n + 1)]
    p = 2
    while(p * p <= n):
        if set_numbers[p] is True:
            for multiple in range(p * p, n + 1, p):
                set_numbers[multiple] = False
        p += 1

    primes = [prime for prime in range(2, n + 1) if set_numbers[prime] is True]
    return primes
