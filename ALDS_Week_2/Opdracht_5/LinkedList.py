class LinkedNode():
    value = None
    next = None

    def __init__(self, value):
        '''Constructor
        Args:
            Param1: value you want to set in this node.
        Returns:
            Nothing
        '''
        self.value = value

    def append(self, value):
        '''Function to append to the linked list of nodes. 
        Args:
            Param1: value you want to append in the linked nodes.
        Returns:
            Nothing
        '''
        if self.next == None:
            self.next = LinkedNode(value)
        else:
            self.next.append(value)

    def delete(self, valueToSearch):
        '''Function to delete a value from the nodes.
        Args:
            Param1: Value to search for and delete.
        Returns:
            Nothing
        '''
        if self.value == valueToSearch:
            self.value = self.next.value
            temp = self.next.next
            self.next.next = None
            self.next = temp
        if self.next != None:
            if self.next.value == valueToSearch:
                self.next.value = None
                self.next = self.next.next
            else:
                self.next.delete(valueToSearch)

    def min(self):
        '''Function to find the minimum value in the array of linked nodes.
        Args:
            None.
        Returns:
            minimum value from the list of linked nodes.
        '''
        if self.value != None:
            if self.next != None:
                temp = self.next.min()
                if temp < self.value:
                    return temp
                else:
                    return self.value
            else:
                return self.value
        else:
            return None


a = LinkedNode(10)
print(a.value)
a.append(11)
print(a.next.value)
a.append(12)
print(a.next.next.value)
a.delete(11)
print(a.value)
print(a.next.value)
a.append(10)
a.append(1)
a.append(100)
print("min: ", a.min())
