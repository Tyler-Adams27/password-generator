"""
The password generator module
"""

import random

def generate(length):
    """
    Generator
    """
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = "!@#$%^&*"
    result = ""
    letter_count = 0
    while letter_count < length:
        try:
            rng = random.randint(1, 10)
            if rng <= 3 and lower_case:
                rng_index = random.randint(0, len(lower_case) - 1)
                result += lower_case[rng_index]
                letter_count += 1
            elif 4 <= rng <= 7 and upper_case:
                rng_index = random.randint(0, len(upper_case) - 1)
                result += upper_case[rng_index]
                letter_count += 1
            elif rng > 7 and symbols:
                symbol_index = random.randint(0, len(symbols) - 1)
                result += symbols[symbol_index]
                letter_count += 1
        except IndexError as e:
            print(f"Index Error (List index out of range): {e}")
        except ValueError as e:
            print(f"Value Error (List might be empty): {e}")
    return result

print(generate(12))

