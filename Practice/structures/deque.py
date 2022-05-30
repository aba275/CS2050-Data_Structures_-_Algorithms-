class Deque:
    """
    a custom deque implementation using a
    Python list to hold the deque
    """
    def __init__(self):
        """
        instantiate a deque and create the
        list that will hold the deque
        """
        self.dequeList = []
        
    def isEmpty(self):
        """
        return true if deque is empty, 
        False otherwise
        """
        return self.dequeList == []

    def addFront(self, new_item):
        """ add an item to the back of the deque(index = -1) """
        self.dequeList.append(new_item)

    def addRear(self, new_item):
        """ add an item to the back of the deque(index = 0) """
        self.dequeList.insert(0,new_item)

    def removeFront(self):
        """ return and remove item from the front of the deque(index = -1)"""
        return self.dequeList.pop()
    
    def removeRear(self):
        """ return and remove item from the Back of the deque(index = -1)"""
        return self.dequeList.pop(0)

    def size(self):
        """ return the number of items in the deque """
        return len(self.dequeList)

    def seeFulldeque(self):
        """this method is not necessary for a fully 
        functional program
        """
        print(self.dequeList)

        