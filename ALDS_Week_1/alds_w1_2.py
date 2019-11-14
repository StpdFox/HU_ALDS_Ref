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

print(getNumbers("friau;h3rpierahnjw9r348aowij9"))