class FlashCard:
    """
    FlashCard Class
    """
    def __init__(self, question=None, options=None, hint=None, answer=None, attempt=0):
        """
        FlashCard class constructor initializing needed values
        """
        self.question = question
        self.options = options
        self.hint = hint
        self.answer = answer
        self.attempt = attempt
        self.next = None


class FlashDeck:
    def __init__(self):
        self.head = None
    """
    push function for flashcards in deck
    """

    def push(self, question, options, hint, answer):
        temp = FlashCard(question, options, hint, answer)

        if self.head is None:
            self.head = temp
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = temp

    """
    Delete function to remove flashcards in deck
    """
    def removeCard(self, key):
        temp = self.head

        if (temp is not None):
            if (temp.question == key):
                self.head = temp.next
                temp = None
                return

        while(temp is not None):
            if temp.question == key:
                break
            prev = temp
            temp = temp.next

        if(temp == None):
            return

        prev.next = temp.next

        temp = None

    """
    Loop that says if list==None, then the quiz is complete
    If list is none, means quiz is completed
    """
    def isEmpty(self):
        current_node = self.head
        if(current_node == None):
            print("You finished the quiz")
            exit()
        return current_node != None

    """
    Main code for test. Starts exam loop and gives out 
    statements accepting input.
    """
    def startTest(self):
        while(self.isEmpty() != None):
            temp = self.head
            """
            loop through give output to user as they input
            """
            while temp is not None:
                print(temp.question)
                print(temp.hint)
                print(temp.options)
                answer = input("Answer: ")

                if(answer == temp.answer):
                    print("Correct! Good Job!")
                    print(" ")
                    temp.attempt = temp.attempt+1
                    if(temp.attempt >= 2):
                        temp2 = temp
                        self.removeCard(temp2.question)
                    temp = temp.next
                else:
                    print("Wrong Answer! Try again later!")
                    print(" ")
                    temp = temp.next
"""
Initialize the list as empty for the test
"""
cllist = FlashDeck()

"""
Main information stored in flashcards, questions, hints,etc...
"""
question = "Who is the CEO of Facebook?"
hint = "(Hint: Name starts with M)"
options = "A. Steve Jobs B. Bill Gates C. Mark Zuckerburg D. Larry Paige"
answer = "C"
cllist.push(question, options, hint, answer)

question = "Convert 1001110 to decimal"
hint = "(Hint: use what we learned in class)"
options = "A. 75 B. 78 C. 59 D. 77"
answer = "B"
cllist.push(question, options, hint, answer)

question = "Who is the founder of Apple?"
options = "A. Steve Jobs B. Bill Gates C. Tim Cook D. Larry Paige"
hint = "(Hint: Name starts with S)"
answer = "A"
cllist.push(question, options, hint, answer)

print("Starting Test...")
"""
start the exam
"""
cllist.startTest()
