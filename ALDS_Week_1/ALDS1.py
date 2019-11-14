def max(arr):
    """
        Function that finds and returns the maximum value of array(list) arr
        Time complexity O(n)
        :param arr: array(list) containing integers
        :return highest: integer containing highest number in arr
        """
    tempMax = float("-inf")
    for nr in arr:
        if nr > tempMax:
            tempMax = nr
    return tempMax


def getNumbers(s):
    """
    Function that turns all numbers in a string to integers and returns them in a list

    :param s: string up for parsing
    :return result: list containing all numbers in the string
    """
    result = []
    buffer = ''

    for i in s:
        if i.isdigit():
            buffer += i
        elif buffer != '':
            result.append(int(buffer))
            buffer = ''

    if buffer != '':
        result.append(int(buffer))

    return result

# 1.3
# ANSWER: het maakt een lijst met de sommen van de lijst met steeds de twee buitenste elementen weggeknipt.
# lst = [1, 2, 3, 4, 5, 6] -> result = {21, 14, 7}


# 1.4
# 500n+100n^1.5+50n*log(n)       	|	100n^1.5   	    |	O(n^1.5)
# 0.3n + 5n ^ 1.5 + 2.5*n1.75       | 5n ^ 1.5          | O(n ^ 1.5)
# n ^ 2log(n) + n(log(n)) ^ 2       | n(log(n)) ^ 2     | O(n(log(n)^ 2)
# nlog(n) + nlog(n)                 | nlog(n)           | O(n)
# 100n + 0.01n ^ 2                  | 0.01n ^ 2         | O(n ^ 2)
# 0.01n + 100n ^ 2                  | 100n ^ 2          | O(n ^ 2)
# 2n + n ^0.5 + 0.5n^1.25		    | 	0.5n^1.25   	|	O(n^1.25)


# 1.5
# % ANSWER:
# addSum1: O(n)
# addSum2: O(n ^ 2)
# addSum3: O(n ^ 2)
# addSum4: O(n ^ 3)
# addSum5: O(n ^ 2)
# addSum6: O(n)

# 1.6


def hairyGroupsOf3(arr):
    result = [(), (), ()]
    m = 0
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                tup = (arr[i], arr[j], arr[k])
                relativeHair = avgHairLength(
                    tup) - (avgHairLength(arr)/avgHairLength(tup))
                result[m] = (tup, relativeHair)
                m += 1
    return result


hairyGroupsOf3.avgHairLength = 0


# Time complexity = O(n^4), assuming that avgHairLength() == O(n)

# result <- an empty array of 3-tuples of length (l over 3)
#m <- 0
#avgHair <- avgHairLength(arr)
# for i $ 0..L-1 do
#    for j $ i+1..L-1 do
#	    for k $ j+1..L-1 do
#		    tup <- (arr[i],arr[j],arr[k]
#			relativeHair <- avgHairLength(tup) - (avgHair/avgHairLength(tup))
#			result[m] <- (tup, relativeHair)
#			m++
#		end for
#	end for
# end for
# return result

# Now it's O(n^3)

# 5

def hairyGroupsOf3New(arr):
    result = [(), (), ()]
    m = 0
    avgHair = avgHairLength(arr)
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                tup = (arr[i], arr[j], arr[k])
                relativeHair = avgHairLength(
                    tup) - (avgHair/avgHairLength(tup))
                result[m] = (tup, relativeHair)
                m += 1
    return result

# 1.7


def find(lst, x):
    """
    Function that finds the index of element x in list lst recursively. If x is not in lst, it returns -1
    :param lst: list
    :param x: element that needs to be found
    :return: integer representing the index of x in lst, or -1 if x not in lst
    """
    if not lst:
        return -1
    if lst[0] == x:
        return 0
    else:
        y = find(lst[1:], x)
        return 1 + y if y > -1 else -1


a = [1, 2, 3, 4, 5, 6, 7, 8]
print(find(a, 7))

# 1.8


def GCD(p, q):
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
        return GCD(q, p % q)
    return GCD(q, p)


# 1.9

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
