class myStack():
    """
    Class to make a stack
    EXAMPLE
    --------
    >>> stack = mystack ()
    """

    def __init__(self):
        """
        Constructor for Class myStack
        PARAMETERS
        ------------
        self : self
        EXAMPLE
        --------
        >>> stack = mystack ()
        """
        self.list = []

    def isEmpty(self):
        """
        Function to check is the stack is empty
        PARAMETERS
        ------------
        self : self
        RETURN
        ---------
        result : bool
        True if and only if the stack is empty .
        EXAMPLE
        --------
        >>> stack = mystack ()
        >>> stack . isEmpty ()
        True
        """
        return bool(self.list)

    def push(self, x):
        """
        Function to push things to the stack
        PARAMETERS
        ------------
        self : self
        x
        :
        The value you want to push onto the stack
        EXAMPLE
        --------
        >>> stack = mystack ()
        >>> stack.push (5)
        """
        self.list.append(x)

    def pop(self):
        """
        Function to pop a value from the stack
        PARAMETERS
        ------------
        self : self
        RETURN
        ---------
        top :
        the top value of the stack
        EXAMPLE
        --------
        >>> stack = mystack ()
        >>> stack . push (15)
        >>> stack . push (5)
        >>> stack . pop ()
        5
        >>> stack . pop ()
        15
        """
        return self.list.pop()

    def peek(self):
        """
        Function to peek at the top variable on the stack .
        PARAMETERS
        ------------
        self : self
        RETURN
        ---------
        top :
        The value that is on the top of the stack
        EXAMPLE
        --------
        >>> stack = mystack ()
        >>> stack . push (15)
        >>> stack . push (5)
        >>> stack . peep ()
        5
        >>> stack . peep ()
        5
        """
        if len(self.list) > 0:
            top = self.list[len(self.list)-1]
            return top
        else:
            return None


a = myStack()
print(a.isEmpty())
a.push(5)

print(a.isEmpty())
