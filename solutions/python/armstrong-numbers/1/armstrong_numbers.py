def is_armstrong_number(number):
    digits = str(number)
    number_of_digits = len(digits)
    sum = 0
    for num in digits:
        sum += int(num) ** number_of_digits
    
    return sum == number