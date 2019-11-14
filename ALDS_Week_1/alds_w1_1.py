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

list = [4,7,9,4,1,613,717,82]

print(max(list))