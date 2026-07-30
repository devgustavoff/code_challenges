import math

def isPrime(candidate):
    for num in range(2, math.floor(candidate ** 0.5) + 1):
        if candidate % num == 0:
            return False
    return True

def primes_generator():
    candidate = 2
    while True:
        if isPrime(candidate):
            yield candidate
            candidate += 1
        else:
            candidate += 1

def prime(number):
    if number < 1:
        raise ValueError("there is no zeroth prime")
    
    count = 0
    primes = primes_generator()
    while count < number:
        num = next(primes)
        count += 1

    return num