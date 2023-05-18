#!/usr/bin/python3
"""module that constains method to validate"""


def validUTF8(data):
    """validates utf 8"""
    num_bytes = 0

    for byte in data:
        # Check if the byte is a continuation byte
        if num_bytes == 0:
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7) != 0:
                return False
        else:
            # Check if the byte is a continuation byte (starts with 10)
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    # If all bytes have been checked and there are no incomplete characters
    return num_bytes == 0
