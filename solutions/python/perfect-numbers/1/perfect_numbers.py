def classify(number: int):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1 or number < 0:
        raise ValueError("Classification is only possible for positive integers.")

    classification_scheme = ""

    factors_numbers = list()
    for n in range(1, number):
        if number % n == 0:
            factors_numbers.append(n)

    if sum(factors_numbers) == number:
        classification_scheme = "perfect"
    elif number < sum(factors_numbers):
        classification_scheme = "abundant"
    elif number > sum(factors_numbers):
        classification_scheme = "deficient"

    return classification_scheme