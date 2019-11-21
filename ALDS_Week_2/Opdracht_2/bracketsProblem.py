from myStack import *


def checkBrackets(string):
    '''function to check if the syntax of a made up language is correct
    Args:
        Param1: String with the made up code
    Returns:
        void or prints a statement with where the error is
    '''
    stack = myStack()
    BracketsDict = {'[': ']', '(': ')', '<': '>'}
    counter = 0
    for character in string:
        counter += 1
        if character not in BracketsDict.keys() and character not in BracketsDict.values():
            errorstring = ''
            for item in BracketsDict.keys():
                errorstring += item
                errorstring += ' '
            for item in BracketsDict.values():
                errorstring += item
                errorstring += ' '
            print("------------------\nError 1: invalid syntax. only ",
                  errorstring[:5], " or ", errorstring[6:], " allowed.")
            return
        elif character in BracketsDict.keys():
            stack.push(character)
            continue
        elif character in BracketsDict.values():
            if stack.isEmpty():
                print("------------------\nError 2: invalid syntax, to many closing characters:",
                      character, " at position", counter)
                return
            openingChar = stack.pop()
            if BracketsDict[openingChar] == character:
                continue
            else:
                print("------------------\nError 3: invalid syntax: ", openingChar, " before",
                      character, " at position", counter, "in line.", BracketsDict[openingChar], "needed")
                return
    if stack.isEmpty():
        print("Valid syntax")
        return
    else:
        print("------------------\nError 4: To many opening brackets")


checkBrackets("(((<>)))")  # goed
checkBrackets("#$%(((<>)))")  # fout, verkeerde karakters
checkBrackets("(((<)>))")  # fout, closing ) verkeerde plek
checkBrackets("(((<>)))]")  # fout, closing ] teveel
checkBrackets("(((<>))))")  # fout, closing ) teveel
checkBrackets("(((<]>))")  # fout, closing ] verkeerde plek
checkBrackets("[(((<>)))")  # fout, teveel openening dingen
