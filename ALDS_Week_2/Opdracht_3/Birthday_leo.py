#opdracht 2.3


from random import randint as randomInt
def birthday_problem(amount_of_students):
    classes = [len(set([randomInt(1,365) for _ in range(amount_of_students)])) for _ in range(100)]
    total =sum(classes)
    return (amount_of_students * 100 - total)/ (amount_of_students * 100)
print(birthday_problem(23))

