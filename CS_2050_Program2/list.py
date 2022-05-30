# Note: this code is not fully documented, and not cleaned up
#       to be thoroughly consistent in its style nor design

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

    def setNext(self,next):
        self.next = next


class UnorderedList:

    # constructor initializes the list to be empty
    def __init__(self):
        self.head = None

    # return True is the list is empty, False otherwise
    def isEmpty(self):
        return self.head == None

    # return the number of Nodes currently in the list
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    # return index of the node with node.data == data if it exists, otherwise -1
    def index(self, data):
        current = self.head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == data:
                found = True
            else:
                current = current.getNext()
                index += 1
        if found:
            return index
        else:
            return -1

    # return True if data exists in the list, False otherwise
    def search(self, data):
        index = self.index(data)
        if index >= 0:
            return True
        else:
            return False

    # add an item to the beginning of the list
    def add(self, data_to_add):
        temp_node = Node(data_to_add)
        temp_node.setNext(self.head)
        self.head = temp_node

    # add a node with its contents equal to data to the back of the list
    def append(self, data):
        current = self.head
        temp_node = Node(data)
        while current.getNext() != None:
            current = current.getNext()
        current.setNext(temp_node)

    # insert a node with data_to_insert into position pos in the list
    def insert(self, pos, data_to_insert):

        # if data_to_insert is to be added at front of list then use add()
        if pos == 0:
            self.add(data_to_insert)

        # if it is to be added to back of the list then use append()
        elif pos == self.size():
            self.append(data_to_insert)

        # if it's to be added somewhere in between then there's a little work to do
        elif pos > 0 and pos < self.size():
            current = self.head
            previous = None
            index = 0
            temp_node = Node(data_to_insert)
            while index < pos:
                previous = current
                current = current.getNext()
                index += 1
            previous.setNext(temp_node)
            temp_node.setNext(current)

        # not a valid position to add a node
        else:
            print("not a valid position in the current list for insertion")

    # remove and return the node at position pos, or at the last position if pos is not given
    def pop(self, pos=None):

        # if position is not given when this method is called, then pop the last node in the list
        if pos == None:
            pos = self.size() - 1

        # check that pos given is a valid position in the list
        if pos < self.size() and pos >= 0:
            current = self.head
            previous = None
            index = 0

            # traverse list until index == pos and current == (item at that position)
            while index < pos:
                previous = current
                current = current.getNext()
                index += 1

            # bypass the current node to remove it from the list then return current
            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
            return current.getData()

        else:
            print("not a valid position in the current list to pop from ")
            return None

    # remove node from the list that has data == data_to_remove
    def remove(self, data_to_remove):
        index_to_remove = self.index(data_to_remove)

        if index_to_remove >= 0:
            self.pop(index_to_remove)
        else:
            print("item", str(data_to_remove), "cannot be removed because it is not in the list")

    # an ad hoc / debugging method to allow for a quick view of the current list in it's entirety
    def seeFullList(self):
        current = self.head
        output = "head -> "
        while current != None:
            output = "".join((output, "["+str(current.getData())+"]", " -> "))
            current = current.getNext()
        output = "".join((output, "None"))
        print(output)


class OrderedList(UnorderedList):

    # override the add method from the UnorderedList class to ensure the list remains sorted
    def add(self, data_to_add):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > data_to_add:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(data_to_add)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    # add should be the only way to an insert a new item in an OrderedList object
    def append(self, data):
        print("cannot use append(data) with OrderedList")

    def insert(self, pos, data):
        print("cannot use insert(pos, data) with OrderedList")


