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
    numbers = list()
    roman_number = list()
    for n in roman_numerals:
        temp = number // n[0]
        roman_number.append(n[1]*temp)
        number = number % n[0]
    return "".join(roman_number)

print(roman(1))