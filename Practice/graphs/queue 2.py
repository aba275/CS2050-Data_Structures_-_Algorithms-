class Queue:
    """
    a custom queue implementation using a
    Python List
    """
    def __init__(self):
        self.queueList = []
        
    def isEmpty(self):
        return self.queueList == []

    def enqueue(self, new_item):
        self.queueList.insert(0,new_item)

    def dequeue(self):
        return self.queueList.pop()

    def peek(self):
        return self.queueList[-1]

    def size(self):
        return len(self.queueList)

    def seeFullqueue(self):
        print(self.queueList)

        