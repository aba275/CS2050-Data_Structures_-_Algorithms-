class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

    def getData(self): 
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data): 
        self.data = data

    def setNext(self, next): 
        self.next = next
    
class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, data):
        temp = Node(data)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None: # while not at the end of the list
            count += 1
            current = current.getNext()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == data:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, data_to_remove):
        """ remove the node with node.data == data_to_remove
        (assuming it is present)
        """
        current = self.head
        previous = None
        found = False
        while not found: # loop to find the position (and set previous)
            if current.getData() == data_to_remove:
                found = True
            else:
                previous = current
                current = current.getNext()
                
        if previous == None: # found was set to True in the first round of the loop
            self.head = current.getNext() # remove what was first item in the list
        else:
            previous.setNext(current.getNest()) # jump over item to be removed

    def append(self, data):
        """ append data to the end of the list """
        current = self.head
        temp = Node(data)
        while current.getNext()!= None:
            current = current.getNext()
        current.setNext(temp)

    def seeFullList(self):
        current = self.head
        while current.getNext() != None:
            print(current.getData())
            current - current.getNext()

    def index(self, data):
        current = self.head
        found = -1

        isFound = False
        while current != None and not isFound:
            if current.getData() != data:
                current = current.getNext()
                return found + 1
            else:
                isFound = True
            found += 1
        return found
    """
    def insert(self, pos, data):
        
        insert data into list before the node/date that is currently at possition pos
        ex: insert(1, dl will insert an object w/ data=d before item currently at pos -1) 
        
        if pos == 0: # insert at beginning
            ???
        elif pos == self.size(): #insert at the end
            ???
        elif pos > 0 and pos < self.size():
            current = self.head
            previous = None
            index = 0
            while index < pos: # exit when reach postiion we want to insert at
                c?
            previous.setNext(temp_node)
            temp_node.setNext(current)
    """
