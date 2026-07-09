def primes(limit):
    numbers = list(range(2, limit + 1))
    is_prime = [True] * len(numbers)
    marked = set()
    for index, number in enumerate(numbers):
        if is_prime[index]:
            for idx in range(index, limit + 1, number):
                if idx != index and idx < len(is_prime):
                    is_prime[idx] = False
                    marked.add(numbers[idx])
    
    return sorted(set(numbers).difference(marked))
print(primes(30))