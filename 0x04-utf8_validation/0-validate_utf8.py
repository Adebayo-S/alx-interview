#!/usr/bin/python3
"""
determines if a given data
set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """validate data for UTF-8"""
    try:
        bytes(data).decode('utf-8')
    except BaseException:
        return False
    return True
