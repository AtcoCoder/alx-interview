#!/usr/bin/python3
""" 0-validate_utf8 module """


def validUTF8(data):
    """validUTF8(data)
    determines if a given data set represents a valid UTF-8 encoding
    data - list of integers
    returns True if data is a valid UTF-8 encoding
    else return False
    """
    for number in data:
        first_8_bits = f'{number:08b}'
        valid_first_bits = ['0', '110', '1110', '11110']
        if first_8_bits[0] in valid_first_bits:
            continue
        elif first_8_bits[:3] in valid_first_bits:
            continue
        elif first_8_bits[:4] in valid_first_bits:
            continue
        elif first_8_bits[:5] in valid_first_bits:
            continue
        else:
            return False
    return True
