#!/usr/bin/python3
"""
Write a method that determines if a given data set represents
a valid UTF-8 encoding.

Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need to handle
the 8 least significant bits of each integer
"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """checks if a or set of data is a valid UTF-8 encoding"""
    n_bytes = 0

    # Masks to check the leading bits of a byte
    mask1 = 1 << 7    # 10000000
    mask2 = 1 << 6    # 01000000

    for num in data:
        mask = 1 << 7
        if n_bytes == 0:
            # Count the number of leading 1s in the first byte
            while mask & num:
                n_bytes += 1
                mask = mask >> 1

            # If no leading 1s, it means it's a 1-byte character (0xxxxxxx)
            if n_bytes == 0:
                continue

            # For UTF-8, a character must be 1 to 4 bytes long
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # For subsequent bytes, they must match the pattern 10xxxxxx
            if not (num & mask1 and not (num & mask2)):
                return False

        # Decrement the number of bytes left to process in the current character
        n_bytes -= 1

    # All characters should be fully processed
    return n_bytes == 0
