#!/usr/bin/python3
'''
    module that finds minimum operations
    coding challenge
'''


def minOperations(n):
    '''
        function that finds minimum operations
    '''
    if not isinstance(n, int):
        return 0
    num_of_operations = 0
    clipboard = 0
    done = 1

    while done < n:
        if clipboard == 0:
            # the first copy all and paste
            clipboard = done
            done += clipboard
            num_of_operations += 2
        elif n - done > 0 and (n - done) % done == 0:
            # copy all and paste
            clipboard = done
            done += clipboard
            num_of_operations += 2
        elif clipboard > 0:
            # paste
            done += clipboard
            num_of_operations += 1
    return num_of_operations
