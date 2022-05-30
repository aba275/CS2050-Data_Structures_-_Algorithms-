from deque import Deque

def palCheck(string):
    """ a function to check whether a string is a palindrome """
    d = Deque()
    # copy the string to our deque object one character at a time
    for char in string:
        d.addRear(char)
    
    while d.size() > 1:
        firstChar = d.removeRear()
        lastChar = d.removeFront()
        if firstChar != lastChar:
            print(string + " is not a palindrome!")
            return False
    
    print(string + " is a palindrome!")
    return True

palCheck('radar')
palCheck('racecar')
palCheck('ini')