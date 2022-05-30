import unittest

class BinHeap:

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def isEmpty(self):
        return self.currentSize == 0

    def size(self):
        pass

    def findMin(self):
        pass

    def insert(self, k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percUp(self, i):
        while i // 2 > 0:
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def percDown(self, i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self, i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval

    def buildHeap(self, alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1



class TestBinaryHeap(unittest.TestCase):
    """ Extend unittest.TestCase and add methods to test HashTable """

    def testSize(self):
        """ Check that BinaryHeap.size() method works """
        bh = BinHeap()
        bh.buildHeap([9, 5, 6, 2, 3])
        self.assertEqual(bh.size(), 5)

    def testIsEmpty(self):
        """ Check that BinaryHeap.isEmpty() method works """
        bh = BinHeap()
        self.assertEqual(bh.isEmpty(), True)
        #bh.buildHeap([9, 5, 6, 2, 3])
        #self.assertEqual(bh.isEmpty(), False)

    def testFindMin(self):
        """ Check that BinaryHeap.findMin() method works """
        bh = BinHeap()
        self.assertEqual(bh.isEmpty(), True)
        bh.buildHeap([9, 5, 6, 2, 3])
        self.assertEqual(bh.findMin(), 2)

    """ add more tests to check heaps are built properly, items added/removed okay, etc. """


def unittest_main():
    print("-"*25, "running unit tests", "-"*25)
    unittest.main()


def main():
    print("-"*25, "running main() ", "-"*25)
    bh = BinHeap()
    bh.buildHeap([9, 5, 6, 2, 3])
    print(bh.heapList)


if __name__ == '__main__':
    main()
    unittest_main()

