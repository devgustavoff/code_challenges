def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")

    count = 0
    result = number

    while result != 1:
        if result % 2 == 0:
            result = result // 2
        else:
            result = result * 3 + 1

        count += 1

    return count