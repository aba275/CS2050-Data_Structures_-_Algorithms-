class Stack:
    """
    a custom stack implementation 
    """

    def __init__(self):
        """
        Instantiate the single field (a list) in a Stack object
        """
        self.items = []

    def isEmpty(self):
        """
        Return boolean based on whether stack contains 1 or more (True) or 0 items (False)
        """
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

