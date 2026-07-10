def primes(limit):
    not_prime = set()
    primes = []

    for num in range(2, limit + 1):
        if num not in not_prime:
            primes.append(num)
            not_prime.update(range(num*num, limit+1, num))
    
    return primes