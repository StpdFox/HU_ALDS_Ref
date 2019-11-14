def findPrimes(max):
    """
    findPrimes(max) finds all primes up to and including value max
    :param max: integer that's used for the upper bound of primes it has to find
    :return: integer list containing all primes up to (and including) max
    """
    primes = []
    not_prime = set()

    for i in range(2, max + 1):
        if i in not_prime:
            continue

        for f in range(i * i, max + 1, i):
            not_prime.add(f)
        primes.append(i)

    return primes


print(findPrimes(1000))


# 2

# O(n log n)

# 3

# See #1

# 4

# O(n log n)
