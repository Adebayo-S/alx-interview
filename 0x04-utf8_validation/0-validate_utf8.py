#!/usr/bin/python3
"""
determines if a given data
set represents a valid UTF-8 encoding
"""

import re


def validUTF8(data):
    """validate data for UTF-8"""
    rgx = b'^(?:[\x00-\x7F]|[\xC2-\xDF][\x80-\xBF]|\xE0[\xA0-\xBF][\x80-\xBF]|\
      [\xE1-\xEC\xEE\xEF][\x80-\xBF]{2}|\xED[\x80-\x9F][\x80-\xBF]|\xF0[\x90-\xBF][\x80-\xBF]\
          {2}|[\xF1-\xF3][\x80-\xBF]{3}|\xF4[\x80-\x8F][\x80-\xBF]{2})*$'
    try:
        byte_data = bytes(data)
        # 1. Add a check for invalid byte sequences
        if not re.match(rgx, byte_data):
            return False
        byte_data.decode('utf-8')
    except BaseException:
        return False
    return True
