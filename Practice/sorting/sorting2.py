def swap_two_elements(alist, pos1, pos2):
    temp = alist[pos1]
    alist[pos1] = alist[pos2]
    alist[pos2] = temp

def swap_to_elements(alist, pos1, pos2):
    alist[pos1], alist[pos2] = alist[pos2], alist[pos1]

def bubblesort(alist):
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                swap_two_elements(alist, i, i+1)