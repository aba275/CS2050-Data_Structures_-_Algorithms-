class Stack:
    def __init__(self):
        self.stackList = []
        
    def isEmpty(self):
        return self.stackList == []

    def push(self, new_item):
        self.stackList.append(new_item)

    def pop(self):
        return self.stackList.pop()

    def peek(self):
        return self.stackList[-1]

    def size(self):
        return len(self.stackList)

    def seeFullStack(self):
        print(self.stackList)

        