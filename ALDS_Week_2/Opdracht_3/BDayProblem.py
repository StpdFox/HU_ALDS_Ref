import random


def generateList(array, nrOfStudents):
    '''Function to fill a list with random numbers between 1 and 356.

    Args:
        Param1: an empty (or filled) list.
        Param2: The number of students i.e. the amount of places in the array you want to fill with a random number.
    Returns:
        void 
    '''
    for i in range(nrOfStudents):
        array.append(random.randrange(1, 357))


def searchDuplicates(array):
    '''Function to search for duplicates in a given array.
    Args:
        Param1: list or tuple to search for duplicates.

    Returns:
        integer with the number of duplicates found.
    '''
    dup = 0
    for index1 in range(len(array)-1):
        for index2 in range(len(array)-1):
            if index1 != index2:
                if array[index1] == array[index2]:
                    dup += 1
    return dup


totalDup = 0
for i in range(100):
    ar = []
    generateList(ar, 50)
    totalDup += searchDuplicates(ar)
print("estimated probability: ", totalDup/100)
