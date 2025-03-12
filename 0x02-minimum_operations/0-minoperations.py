#!/usr/bin/python3
'''
    module that finds minimum operations
    coding challenge

    In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0
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
