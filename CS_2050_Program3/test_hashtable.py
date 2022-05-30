import hashtable
import timeit
import random
import matplotlib.pyplot as plt

hm = hashtable.HashTable


def hashTableRetrieval():
    return h[key_to_retrieve]

t = list()

hashtable_size = 10027
predetermined_load_factor = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
number_unique_keys = 13

for lf in predetermined_load_factor:
    h = hashtable.HashTable(hashtable_size)
    items_to_store = [random.randint(0, number_unique_keys) for x in range(round(lf*hashtable_size))]
    key_to_retrieve = max(items_to_store)
    for v in items_to_store:
        h[v] = 'hello' + str(v)

    t.append(timeit.timeit("hashTableRetrieval()", "from __main__ import hashTableRetrieval", number=1000)/1000)


plt.plot(predetermined_load_factor, t, color='blue')
plt.title('Retreiving/searching a HashTable of size = ' + str(hashtable_size))
#plt.ylim((0, 0.0001))

plt.show()

