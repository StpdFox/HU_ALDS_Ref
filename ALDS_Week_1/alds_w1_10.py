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
    sorted_change = []
    new_sorted_change = []

    for last_used_coin in coins:
        combos = find_change(n - last_used_coin, coins)
        for combo in combos:
            combo.append(last_used_coin)
            combo = sorted(combo)
            if combo not in all_changes:
                all_changes.append(combo)
    # for i in all_changes:
    #     sorted_change.append(sorted(i))
    # for elem in sorted_change:
    #     if elem not in new_sorted_change:
    #         new_sorted_change.append(elem)
    # all_changes = new_sorted_change
    return all_changes


m = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

print(find_change(7, m))
