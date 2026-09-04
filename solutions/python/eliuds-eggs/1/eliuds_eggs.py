def egg_count(display_value):
    binary_number = list()
    division_result = 0
    counter = 0
    while display_value != 0:
        division_result = display_value // 2
        remaider = display_value % 2
        if remaider == 1:
            counter += 1
        binary_number.append(remaider)
        display_value = division_result

    return counter