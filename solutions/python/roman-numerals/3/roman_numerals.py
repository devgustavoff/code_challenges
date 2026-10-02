roman_numerals = (
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I")
)

def roman(number):
    roman_number = list()
    for value, char in roman_numerals:
        if number == 0:
            break
        temp = number // value
        roman_number.append(char*temp)
        number = number % value
    return "".join(roman_number)