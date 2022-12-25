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
        tmp = number
        while len(str(tmp)) > 5:
            if tmp == 7:
                return True
            # Double the last digit of the number
            last_digit = int(str(tmp)[-1])
            # Subtract it from the rest of the number
            rest_of_number = int(str(tmp)[:-1])
            # Update tmp number
            tmp = 5 * last_digit + rest_of_number

        # Double the last digit of the number
        last_digit = int(str(tmp)[-1])
        # Subtract it from the rest of the number
        rest_of_number = int(str(tmp)[:-1])
        # Check if the result is divisible by 7

        return (5 * last_digit + rest_of_number) % 7 == 0
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
        if number == 13:
            return True
        # Double the last digit of the number
        last_digit = int(str(number)[-1])
        # Subtract it from the rest of the number
        rest_of_number = int(str(number)[:-1])
        # Check if the result is divisible by 7
        return (4 * last_digit + rest_of_number) % 13 == 0
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
        if number == 17:
            return True
        tmp = number
        while len(str(tmp)) > 5:
            # Double the last digit of the number
            last_digit = int(str(tmp)[-1])
            # Subtract it from the rest of the number
            rest_of_number = int(str(tmp)[:-1])
            # Update tmp number
            tmp = rest_of_number - 5 * last_digit

        # Double the last digit of the number
        last_digit = int(str(tmp)[-1])
        # Subtract it from the rest of the number
        rest_of_number = int(str(tmp)[:-1])

        # Check if the result is divisible by 7
        return (rest_of_number - 5 * last_digit) % 17 == 0

    # Check for divisibility by 18
    elif divisor == 18:
        return is_divisible(number, 2) and is_divisible(number, 9)
    # Check for divisibility for 19
    elif divisor == 19:
        if number == 19:
            return True

        tmp = number
        while len(str(tmp)) > 5:
            if tmp == 19:
                return True
            # Double the last digit of the number
            last_digit = int(str(tmp)[-1])
            # Subtract it from the rest of the number
            rest_of_number = int(str(tmp)[:-1])
            # Update tmp number
            tmp = 2 * last_digit + rest_of_number

        # Double the last digit of the number
        last_digit = int(str(tmp)[-1])
        # Subtract it from the rest of the number
        rest_of_number = int(str(tmp)[:-1])

        # Check if the result is divisible by 7
        return (2 * last_digit + rest_of_number) % 19 == 0

    # Check for divisibility by 20
    elif divisor == 20:
        return is_divisible(number, 4) and is_divisible(number, 5)
    # Check for divisibility by 21
    elif divisor == 21:
        print(is_divisible(number,3), is_divisible(number,7))
        return is_divisible(number, 3) and is_divisible(number, 7)
    # Check for divisibility by 22
    elif divisor == 22:
        return is_divisible(number, 11) and is_divisible(number, 2)
    # Check for divisibility by 23
    elif divisor == 23:
        if number == 23:
            return True

        tmp = number
        while len(str(tmp)) > 5:
            if tmp == 23:
                return True
            # Double the last digit of the number
            last_digit = int(str(tmp)[-1])
            # Subtract it from the rest of the number
            rest_of_number = int(str(tmp)[:-1])
            # Update tmp number
            tmp = 7 * last_digit + rest_of_number

        # Double the last digit of the number
        last_digit = int(str(tmp)[-1])
        # Subtract it from the rest of the number
        rest_of_number = int(str(tmp)[:-1])

        # Check if the result is divisible by 7
        return (7 * last_digit + rest_of_number) % 23 == 0
    else:
        return number%divisor == 0

