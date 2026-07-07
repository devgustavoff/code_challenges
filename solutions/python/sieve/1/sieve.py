def primes(limit):
    numbers = [n for n in range(2, limit+1)]
    not_is_prime = []
    for n in numbers:
        for num in range(n, limit+1, n):
            if num != n:
                not_is_prime.append(num)
    
    return list(set(numbers).difference(not_is_prime))