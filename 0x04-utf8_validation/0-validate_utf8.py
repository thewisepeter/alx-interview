#!/usr/bin/python3
'''
    Write a method that determines if a given data set
    represents a valid UTF-8 encoding.

    Prototype: def validUTF8(data)
    Return: True if data is a valid UTF-8 encoding, else
    return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you
    only need to handle the 8 least significant bits of each
    integer
'''


def validUTF8(data):
    '''
        determines if a given data set represents a valid UTF-8
        encoding
    '''

    def isContinuation(byte):
        return (byte & 0b11000000) == 0b10000000

    # Iterate through the data
    i = 0
    while i < len(data):
        # Determine the number of bytes for the current character
        num_bytes = 0
        mask = 0b10000000
        while data[i] & mask:
            num_bytes += 1
            mask >>= 1

        # Check if the number of bytes is within the valid range (1 to 4)
        if num_bytes < 1 or num_bytes > 4:
            return False

        # Check if the following bytes are valid continuation bytes
        for j in range(1, num_bytes):
            i += 1
            if i >= len(data) or not isContinuation(data[i]):
                return False

        i += 1  # Move to the next character

    return True
