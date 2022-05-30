import timeit
import random
import matplotlib.pyplot as plt


# retrieve index of 500 in myList
def listIndex():
    i = myList.index(500)

t1 = list()

values = list(range(1000, 50000, 5000))

for v in values:

    # index a sorted list
    myList = list(range(v))
    t1.append(timeit.timeit("listIndex()", "from __main__ import listIndex", number=1000)/1000)

    # index a randomly shuffled list
    # ...

plt.plot(values, t1, color='red')
plt.legend(('index() w/ sorted list'), loc='upper left')
plt.title('Runtimes for list.index()')

plt.show()