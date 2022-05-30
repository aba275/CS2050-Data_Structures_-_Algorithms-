"""
Title: Assignment #3
Desc: We will be extending the original hastable.py by modyifying 
and overriding various functions, operations, and methods
"""
import unittest
"""
    A class to represent a basic HashTable, which is essentially
    a crude implementation of Python's dict(tionary) class

    Attributes/Fields
    -----------------
    capacity : int 
        size of hastable instance indicating the maximum capacity
    size : int
        size of hashtable instance representing total capacity
    slots: list
        list object to store keys after hashing - at location: hash(key)
    data: list
        list object to store data after hashing - at location: hash(key)
    Methods
    -------
    put(key, data)
    resize()
    hashfunction(key, size)
    rehash(oldhash, size)
    get(key)
    __getitem__(key)
    __setitem__(key, data)
    __len__()
    __contains__(key)
    __delitem__(key)
"""


class HashTable:
    def __init__(self, size):
        """
        HashTable class construction initializing needed values
        setting the max capacity of the hashtable to 1000
        """
        self.capacity = 13
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        """
        Using a function to increase the hashtable when full to the next 
        prime number
        while also using a function to replace keys/slots
        """
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:  # replace data currently there
                self.data[hashvalue] = data  # since exact same key is used
            else:
                if not None in self.slots:
                    # Increase the size of the hashtable to the next prime number
                    self.resize()

                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace data currently there

    def resize(self):
        """
        resize function used for when the hashtable is full 
        The function calculated the next prime number and sets
        the hashtable to that size
        """
        def nextprime():
            new = self.size + 1
            for i in range(new, self.capacity):
                for x in range(2, i):
                    if (i % x) == 0:
                        break
                else:
                    return i

        nextprime = nextprime()
        print('Resizing hashtable from: %d to %d' % (self.size, nextprime))
        self.slots = self.slots + [None] * (nextprime - self.size)
        self.data = self.data + [None] * (nextprime - self.size)
        self.size = nextprime

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        """
        takes the input and rehashes +1
        """
        return (oldhash + 1) % size

    def get(self, key):
        """
        get method sets all initial data to none starting with entry slot
        ajusts data and keys accordingly and takes input from hashfunction
        and rehash
        """
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        """
        gets key value
        """
        return self.get(key)

    def __setitem__(self, key, data):
        """
        sets keys value
        """
        self.put(key, data)

    def __len__(self):
        """
        override len function and return items in table using counter
        """
        counter = 0
        for i in self.data:
            if i is not None:
                counter += 1
        return counter

    def __contains__(self, key):
        """
        override in operator and returns boolean if value is found in the table
        """
        return key in self.slots

    def __delitem__(self, key):
        """
        override del operator and allows for values to be added/removed from the table
        also controls collisions by replacing the value.
        """
        if key in self.slots:
            pos = self.slots.index(key)
            self.slots[pos] = None
            self.data[pos] = None
        print('self.slots[key]:', self.slots)
        print('self.data [value]:', self.data)


class TestHashTable(unittest.TestCase):
    """ Extend unittest.TestCase and add methods to test HashTable """

    def testKeysAfterPuts(self):
        """ Check that hashtable keys are as expected for simple case """
        h = HashTable(7)
        h[6] = 'cat'
        h[11] = 'dog'
        h[21] = 'bird'
        h[27] = 'horse'
        expected = [21, 27, None, None, 11, None, 6]
        self.assertEqual(h.slots, expected)

    def testDataAfterPuts(self):
        """ Check that hashtable data is as expected for simple case """
        h = HashTable(7)
        h[6] = 'cat'
        h[11] = 'dog'
        h[21] = 'bird'
        h[27] = 'horse'
        expected = ['bird', 'horse', None, None, 'dog', None, 'cat']
        self.assertEqual(h.data, expected)

# main() - run any example/demo you want to when running as standalone program


def main():
    h = HashTable(7)
    h[16] = 'cat'
    h[11] = 'dog'
    h[21] = 'bird'
    print("-"*25, "keys and values:", "-"*25)
    print(h.slots)
    print(h.data)
    print(h[16] == 'cat')

# unittest_main() - run unittest's main, which will run TestHashTable's methods


def unittest_main():
    print("-"*25, "running unit tests", "-"*25)
    unittest.main()


# evaluates to true if run as standalone program (e.g. $ python hashtable.py)
if __name__ == '__main__':
    main()
    unittest_main()
