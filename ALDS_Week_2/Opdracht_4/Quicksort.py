import random
counter = 0


def partition(ar, low, high):
    '''Function that puts all smaller numbers than a pivot on the left of himself, and all bigger numbers on the right. It also
    adds to a (global) counter called counter so you can see how much compares it does for a given list
    Args:
        Param1: the array to sort
        Param2: (integer) the low index number from where you want to compare 
        Param3: (integer) the high index number to where you want to compare

    returns:
        a counter for the next use of this function
    '''
    global counter
    pivot = ar[high]
    i = low
    for j in range(low, high):
        if ar[j] <= pivot:
            ar[i], ar[j] = ar[j], ar[i]
            i += 1
        counter += 1
    ar[i], ar[high] = ar[high], ar[i]
    return i


def quickSort(ar, low, high):
    '''Function that recursivly calls the partition function to break up a list in smaller pieces and sorts the given array
    Args:
        Param1: the array to sort
        Param2: (integer) the low index number from where you want to sort 
        Param3: (integer) the high index number to where you want to sort 
    Returns:
        a list with all numbers sorted
        '''
    if low >= high:
        return ar
    p = partition(ar, low, high)
    a = quickSort(ar, low, p-1)
    a = quickSort(ar, p+1, high)
    return ar


def generateRandomList(length):
    '''Function to make a list and fill the list with random numbers between 1 and 1000.

    Args:
        Param1: the maximum length of the list.
    Returns:
        list, filled with random numbers (integers)
    '''
    array = []
    for i in range(length+1):
        array.append(random.randrange(1, 1001))
    return array


for i in range(101):
    array = generateRandomList(100)
    quickSort(array, 0, len(array)-1)

print("average number of compares after 100 lists with 100 items with random values: ",
      round(counter/100, 2))


def partitionMin(ar, low, high):
    '''Function that puts all smaller numbers than a pivot (which is the smallest number in the list) on the left of himself, 
    and all bigger numbers on the right. It also
    adds to a (global) counter called counter so you can see how much compares it does for a given list, to use the lowest number
    in the array, it also uses a global list called templist. In which the smalles pivot is searched and removed for the next iteration.
    Args:
        Param1: the array to sort
        Param2: (integer) the low index number from where you want to compare 
        Param3: (integer) the high index number to where you want to compare

    returns:
        a counter for the next use of this function
    '''
    global counter
    global templist
    pivot = min(templist)
    templist.remove(pivot)
    i = low
    for j in range(low, high):
        if ar[j] <= pivot:
            ar[i], ar[j] = ar[j], ar[i]
            i += 1
        counter += 1
    ar[i], ar[high] = ar[high], ar[i]
    return i-1


def quickSortMin(ar, low, high):
    '''Function that recursivly calls the partition function to break up a list in smaller pieces and sorts the given array
    Args:
        Param1: the array to sort
        Param2: (integer) the low index number from where you want to sort 
        Param3: (integer) the high index number to where you want to sort 
    Returns:
        a list with all numbers sorted
        '''
    if low >= high:
        return ar
    p = partitionMin(ar, low, high)
    a = quickSortMin(ar, low, p-1)
    a = quickSortMin(ar, p+1, high)
    return ar


for i in range(1001):
    array = generateRandomList(100)
    templist = array.copy()
    quickSortMin(array, 0, len(array)-1)

print("average number of compares after 1000 lists with 100 items with random values: ",
      round(counter/1000, 2))
