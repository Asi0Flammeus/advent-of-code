def is_divisible(number, divisor):
    """Returns True if `number` is divisible by `divisor`, False otherwise."""
    # Check for divisibility by 2
    if divisor == 2:
        return int(str(number)[-1]) % 2 == 0
    # Check for divisibility by 3
    elif divisor == 3:
        digit_sum = sum(int(digit) for digit in str(number))
        return digit_sum % 3 == 0
    # Check for divisibility by 4
    elif divisor == 4:
        return int(str(number)[-2:]) % 4 == 0
    # Check for divisibility by 5
    elif divisor == 5:
        return int(str(number)[-1]) in [0, 5]
    # Check for divisibility by 6
    elif divisor == 6:
        return is_divisible(number, 2) and is_divisible(number, 3)
    # Check for divisibility by 7
    elif divisor == 7:
        # Double the last digit of the number
        double_last_digit = int(str(number)[-1]) * 2
        # Subtract it from the rest of the number
        rest_of_number = int(str(number)[:-1])
        # Check if the result is divisible by 7
        return (rest_of_number - double_last_digit) % 7 == 0
    # Check for divisibility by 8
    elif divisor == 8:
        return int(str(number)[-3:]) % 8 == 0
    # Check for divisibility by 9
    elif divisor == 9:
        digit_sum = sum(int(digit) for digit in str(number))
        return digit_sum % 9 == 0
    # Check for divisibility by 10
    elif divisor == 10:
        return int(str(number)[-1]) == 0
    # Check for divisibility by 11
    elif divisor == 11:
        alternating_sum = sum(int(str(number)[i]) if i % 2 == 0 else -int(str(number)[i]) for i in range(len(str(number))))
        return alternating_sum % 11 == 0
    # Check for divisibility by 12
    elif divisor == 12:
        return is_divisible(number, 3) and is_divisible(number, 4)
    # Check for divisibility by 13
    elif divisor == 13:
        digit_sum = sum(int(str(number)[i]) * (13 ** (len(str(number)) - i - 1)) for i in range(len(str(number))))
        return digit_sum % 13 == 0
    # Check for divisibility by 14
    elif divisor == 14:
        return is_divisible(number, 2) and is_divisible(number, 7)
    # Check for divisibility by 15
    elif divisor == 15:
        return is_divisible(number, 3) and is_divisible(number, 5)
    # Check for divisibility by 16
    elif divisor == 16:
        return int(str(number)[-4:]) % 16 == 0
    # Check for divisibility by 17
    elif divisor == 17:
        alternating_sum = sum(int(str(number)[i]) * (17 ** (len(str(number)) - i - 1)) for i in range(len(str(number))))
        return alternating_sum % 17
    # Check for divisibility by 18
    elif divisor == 18:
        return is_divisible(number, 2) and is_divisible(number, 9)
    # Check for divisibility for 19
    elif divisor == 19:
        # Add up the digits of the number
        digit_sum = sum(int(digit) for digit in str(number))
        # Check if the sum is divisible by 19
        return digit_sum % 19 == 0
    # Check for divisibility by 20
    elif divisor == 20:
        return is_divisible(number, 4) and is_divisible(number, 5)
    # Check for divisibility by 21
    elif divisor == 21:
        return is_divisible(number, 3) and is_divisible(number, 7)
    # Check for divisibility by 22
    elif divisor == 22:
        return is_divisible(number, 11) and is_divisible(number, 2)
    # Check for divisibility by 23
    elif divisor == 23:
        # Multiply each digit of the number by the corresponding power of 23, starting from the right
        weighted_sum = sum(int(digit) * (23 ** i) for i, digit in enumerate(reversed(str(number))))
        # Check if the sum is divisible by 23
        return weighted_sum % 23 == 0

for i in range(24):
    print(i,is_divisible(i,i))
