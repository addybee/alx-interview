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
    # perform a bitwise and on each item in data (item & 128 == 0)
    # to see if it is 0
    # store the bitwise operation on each item that yield truth in result
    result = [
        (item & 128) == 0 for item in data if item <= 128
    ]
    # compare the length of the data and result to see if they are equal:
    # if they are not it means some of the integer are not valid utf-8 encoding
    # but if they are equal it means they are all valid utf-8 character
    if len(result) != len(data):
        return False
    return True
