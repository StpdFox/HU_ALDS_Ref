def paid(amount):
    """
    Consider m as the list with all possible coins and banknotes
    and matrix A, where A[i,j] is the number of combinations you
    can pay amount j with the coins and banknotes m[0] up to
    uncluding m[i] Then the following rules can be applied:


    A[i,0] = 1 for all i
    A[0,j] = 1 for all j
    if j >= m[i] then A[i,j] = A[i - 1, j] + A[i,j - m[i]]
    if j < m[i] then A[i,j] = A[i - 1,j]
    """


def find_change(n, coins):
    if n < 0:
        return []
    if n == 0:
        return [[]]
    all_changes = []

    for last_used_coin in coins:
        combos = find_change(n - last_used_coin, coins)
        for combo in combos:
            combo.append(last_used_coin)
            combo = sorted(combo)
            if combo not in all_changes:
                all_changes.append(combo)
    return all_changes


m = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]


def fill(A, until):
    """
        Function fill
        function for filling  A until needed with None 

        PARAMETERS:
        A : list
        B : integer     
    """
    l = len(A)
    until = until+2 - l
    #temp = [None for i in range(len(m))]
    for i in range(until):
        A.append([None for i in range(len(m))])
    # print(len(A))


def money(bedrag,  x=12):
    """
        Function functie
        function for amount of combinations their can be paid
        PARAMETERS:
        bedrag : integer
        x : the rate of m[0:limter] that much be  watched

        RETURNS:
        A[bedrag][x] : the value out of the matrix

        EXAMPLE:

        >>>functie(900)
        173946022
        >>>functie(9)
        8


    """
    if bedrag > (len(A)-1):
        fill(A, bedrag)
    if (bedrag < 0)or (x < 0):
        return 0
    if bedrag == 0:
        return 1
    if A[bedrag][x] != None:
        return A[bedrag][x]
    if bedrag >= m[x]:
        A[bedrag][x] = money(bedrag, x - 1) + money(bedrag - m[x], x)
        return A[bedrag][x]
    return money(bedrag, x-1)


m = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

A = [[None for i in range(len(m))] for i in range(1)]
A[0] = [1 for i in range(len(m))]

print(money(6))
print(money(7))
print(money(8))
