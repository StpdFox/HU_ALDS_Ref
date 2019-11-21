class ListNode:
    """
    Class to make a Linked List
    EXAMPLE
    --------
    >>> linkLst = ListNode()
    """

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def __del__(self):
        return

    def __repr__(self):
        if self.next is None:
            return str(self.data)
        return str(self.data) + self.next.__repr__()

    def append(self, value):
        """
        Function to add a value to the linked list

        PARAMETERS
        ------------
        self : self
        value :
                The value to add to the linked list
        EXAMPLE
        --------
        >>> LinkedList = ListNode ()
        >>> LinkedList . append (15)
        """
        if self.next == None:
            self.next = ListNode(value)
        else:
            self.next.append(value)

    def delete(self, value, prev=None):
        """
        Removes all occurrences of the value from the linked list
        PARAMETERS
        ------------
        self : self
        value :
                The value to be removed from the list
        EXAMPLE
        --------
        >>> LinkedList = ListNode ()
        >>> LinkedList . append (15)
        >>> LinkedList . delete (15)
        """
        while self.data == value:
            if self.next != None:
                self.data = self.next.data
                self.next = self.next.next
            else:
                if prev != None:
                    prev.next = None
                self.__del__
                break

        if self.next != None:
            self.next.delete(value, self)

    def min(self):
        """
        Returns the minimum value of the LinkedList
        PARAMETERS
        ------------
        self : self
        EXAMPLE
        --------
        >>> LinkedList = ListNode ()
        >>> LinkedList . append (3)
        >>> LinkedList . append (15)
        >>> LinkedList . min ()
        3
        """
        if self.data != None:
            if self.next != None:
                tmp = self.next.min()
                if tmp < self.data:
                    return tmp
                else:
                    return self.data
            else:
                return self.data
        return None
