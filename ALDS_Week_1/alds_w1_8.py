def GCD_1(p, q):
    """
    Finds the Greatest Common Divisor of integers p and q using Euclid's algorithm (recursively)
    :param p: integer
    :param q: integer
    :return: integer representing the Greatest Common Divisor of p and q
    """
    if not q:
        return p
    if p == q:
        return p
    if p > q:
        return GCD_1(q, p % q)

    return GCD_1(q, p)


def GCD_2(p, q):
    if (p > q):
        if (q == 0):
            return p
        else:
            return GCD_2(q, p % q)
    else:
        return p


GCD_3 = lambda p, q: p if not q or p == q else (GCD_3(q, p % q) if p > q else GCD_3(q, p))

# Geen rekening gehouden met als Q het hoogste getal is
print(GCD_2(128, 96))
print(GCD_1(128, 96))


print(GCD_3(128,96))

gcd = lambda p, q: p if not q or p == q else (gcd(q, p % q) if p > q else gcd(q, p))