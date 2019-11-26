import random


def sameBirthdatProbability(numberofstudents):
    numberofsamebirthdays = 0
    repeatNTimes = 100
    for i in range(repeatNTimes):
        birthdays = [random.randint(1, 365) for _ in range(numberofstudents)]
        duplicates = set()
        for x in birthdays:
            if birthdays.count(x) > 1:
                duplicates.add(x)
        if len(duplicates) >= 1:
            numberofsamebirthdays += 1
    result = numberofsamebirthdays / 100 * repeatNTimes
    return result


print(sameBirthdatProbability(20))
