#!/usr/bin/python3
''' module that finds min operations'''


def minOperations(n):
    ''' function to find min operations '''
    # If n is less than 2, it's impossible to achieve
    if not isinstance(n, int):
        return 0
   
    if n < 2:
        return 0

    dp = [float('inf')] * (n + 1)

    # The base case: 0 operations needed for 1 H character
    dp[1] = 0

    # Iterate through all possible positions up to n
    for i in range(2, n + 1):
        ''' Try to paste the current content or copy-paste
            from a previous position
        '''
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    '''
        If dp[n] is still infinity, it means it's impossible
        to achieve n H characters
    '''
    return dp[n] if dp[n] != float('inf') else 0
