class PriorityQueue:
    array = []

    def queue(self, value, priority):
        '''Function to set a value and a priority in the queue

        Args:
            Param1: Value you want to place in the priority queue
            Param2: The priority you want to acknowledge to the value
        Returns:
            void
        '''
        tup = (value, priority)
        self.array.append(tup)

    def dequeue(self):
        '''Function to deque the item with the highest priority
            Args:
                None
            Returns:
                the item with the highest priority
        '''
        counter = 0
        max = self.array[0]
        for item in self.array:
            if item[1] > max[1]:
                max = item
        self.array.remove(max)
        return max

    def contains(self, value):
        '''Function to check if a value is in the priority queue
            Args: 
                Param1: the value you want to search for
            Returns:
                boolean
        '''
        for item in self.array:
            if item[0] == value:
                return True
        return False

    def remove(self, value):
        '''Function to remove all elements that hold a given value out of the priority queue
            Args:
                Param1: The value you want to remove from the queue

            Returns:
                Void
        '''
        for item in self.array:
            if item[0] == value:
                self.array.remove(item)
                # was nodig omdat hij anders het laatste element anders niet verwijderde.
                self.remove(value)
                break


a = PriorityQueue()
a.queue(5, 8)
a.queue(10, 3)
print(a.array)
a.queue(3, 4)
a.queue(6, 40)
print(a.array)
print(a.dequeue())
print(a.array)
print(a.contains(1))
print(a.contains(5))
a.queue(10, 10)
a.queue(10, 5)
print(a.array)
a.remove(10)
print(a.array)
