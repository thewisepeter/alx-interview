#!/usr/bin/python3
'''
    Maria and Ben are playing a game. Given
    a set of consecutive integers starting
    from 1 up to and including n, they take
    turns choosing a prime number from the set
    and removing that number and its multiples
    from the set. The player that cannot make a
    move loses the game.

    They play x rounds of the game, where n may be
    different for each round. Assuming Maria always
    goes first and both players play optimally, determine
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
    Ben wins because there are no prime numbers left for Maria
    to choose
    Second round: 5

    Maria picks 2 and removes 2, 4, leaving 1, 3, 5
    Ben picks 3 and removes 3, leaving 1, 5
    Maria picks 5 and removes 5, leaving 1
    Maria wins because there are no prime numbers left for Ben
    to choose
    Third round: 1

    Ben wins because there are no prime numbers for Maria to
    choose
'''


# def is_prime(num):
#     '''
#         checks if a number is a prime number
#     '''
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True


# def isWinner(x, nums):
#     '''
#         determines who the winner is
#     '''
#     maria_wins = 0
#     ben_wins = 0

#     for n in nums:
#         # Initialize a set of integers from 1 to n
#         remaining_numbers = set(range(1, n + 1))

#         # While there are still integers in the set
#         while remaining_numbers:
#             # Maria's turn
#             maria_moves = False
#             for num in sorted(remaining_numbers):
#                 if is_prime(num):
#                     # Remove the prime number and its multiples
#                     for multiple in range(num, n + 1, num):
#                         remaining_numbers.discard(multiple)
#                     maria_moves = True
#                     break
#             if not maria_moves:
#                 # Maria cannot make a move, Ben wins
#                 ben_wins += 1
#                 break

#             # Ben's turn
#             ben_moves = False
#             for num in sorted(remaining_numbers):
#                 if is_prime(num):
#                     # Remove the prime number and its multiples
#                     for multiple in range(num, n + 1, num):
#                         remaining_numbers.discard(multiple)
#                     ben_moves = True
#                     break
#             if not ben_moves:
#                 # Ben cannot make a move, Maria wins
#                 maria_wins += 1
#                 break

#     # Determine the winner
#     if maria_wins > ben_wins:
#         return "Maria"
#     elif maria_wins < ben_wins:
#         return "Ben"
#     else:
#         return None

def isWinner(x, nums):
    '''
        function that checks for the winner
    '''
    if not nums or x < 1:
        return None
    max_num = max(nums)

    my_filter = [True for _ in range(max(max_num + 1, 2))]
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not my_filter[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            my_filter[j] = False
    my_filter[0] = my_filter[1] = False
    y = 0
    for i in range(len(my_filter)):
        if my_filter[i]:
            y += 1
        my_filter[i] = y
    player1 = 0
    for x in nums:
        player1 += my_filter[x] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
