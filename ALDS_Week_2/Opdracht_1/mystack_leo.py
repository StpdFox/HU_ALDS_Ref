# opdr 2.1
class mystack:
    """
    class mystack(), class that works as a stack
    """

    def __init__(self):
        """
        function init(self) that initialize the class.
        ----------------------------------------------------------------------
        PARAMETER:
        self : self
        ----------------------------------------------------------------------
        EXAMPLE:

        >>>a = mystack()
        """
        self.stack = []

    def push(self, a):
        """
        function push(self,a), function that pushes value a on the stack.
        -------------------------------------------------------------------
        PARAMETERS:
        self : self
        a : (can be a value that is able to append in a list)
        -------------------------------------------------------------------
        RETURNS:
        ' pushed ' 
        -----------------------------------------------------------------
        EXAMPLE:
        >>>a.push(56)
        ' pushed ' 
        """
        self.stack.append(a)

    def pop(self):
        """
        function pop(self), pops the top value of the stack and removes them.
        -------------------------------------------------------------------------
        PARAMETERS:
        self : self
        -------------------------------------------------------------------------
        RETURNS:
        ' stack is empty' : string (if the stack is empty)
        a :  variable (that is on the top please of the stack)
        -------------------------------------------------------------------------
        EXAMPLE:
        >>>b = mystack()
        >>>b.pop()
        ' stack is empty '
        >>>b.push(8)
        ' pushed '
        >>>b.pop()
        8
        """
        if not self.stack:
            return self.stack.pop()
        print("is empty")

    def peek(self):
        """
        function peek(self), function that gives top value of stack with out removing it.
        -------------------------------------------------------------
        PARAMETERS:
        self : self
        -----------------------------------------------------------
        RETURNS:
        ' stack is empty' : string (if the stack is empty)
        a :  variable (that is on the top please of the stack)
        -----------------------------------------------------------
        EXAMPLE:
        >>> b= mystack()
        >>>b.peek()
        ' stack is empty ' 
        >>>b.push(5)
        ' pushed '
        >>>b.push(9)
        ' pushed '
        >>>b.peek()
        9
        >>>b.pop()
        9
        """
        if not self.stack:
            return self.stack[-1]
        print("is empty")

    def isEmpty(self):
        """
        function isEmpty, function that empties the hole stack.
        --------------------------------------------------------
        PARAMETERS:

        self : self
        --------------------------------------------------------
        RETURNS:

        'stack is empty' : string
        ----------------------------------------------------------
        EXAMPLE:

        >>> b= mystack()
        >>> b.push(9)
        >>> b.push(8)
        >>> b.isEmpty()
        'stack is empty'
        >>> b.peek()
        'stack is empty'
        """
        return not self.stack


a = mystack()
print(a.isEmpty())
print(a.push(1))
print(a.isEmpty())
