class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class myll:
    def __init__(self):
        self.head = None

    def push(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            self.head = NewNode
            return
        laste = self.head
        while(laste.next):
            laste = laste.next
        laste.next=NewNode
# Function to remove node
    def pop(self, Removekey):

        HeadVal = self.head

        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next

        HeadVal = None

    def print(self):
        printv = self.head
        while (printv):
            print(printv.data),
            printv = printv.next


flashcard = myll()
while(1):
    print("1. Add flash card")
    print("2. remove flash card")
    print("3. print flash deck")
    print("4. Exit")
    op = int(input());
    if(op == 1):
        print("Enter data : ")
        data = input();
        flashcard.push(data)
    if(op == 2):
        print("Enter data : ")
        data = input();
        flashcard.pop(data)
    if(op == 3):
        flashcard.print();
    if(op == 4):
        break;