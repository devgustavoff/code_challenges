def is_armstrong_number(number):
    digits = str(number)
    number_of_digits = len(digits)
    result = 0
    for num in digits:
        result += int(num) ** number_of_digits
    
    return result == number