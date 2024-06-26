#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data: list) -> bool:
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Mask to check the leading bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        # Get the 8 least significant bits of the number
        byte = num & 0xFF

        # If we are at the start of a new UTF-8 character
        if num_bytes == 0:
            # Determine the number of bytes in this UTF-character
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            # If num_bytes is 0, it is a 1-byte character
            if num_bytes == 0:
                continue

            # If num_bytes is more than 4 or 1, it is invalid
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # check that byte starts with 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False
        # Decrement the number of bytes to check
        num_bytes -= 1

    return num_bytes == 0
