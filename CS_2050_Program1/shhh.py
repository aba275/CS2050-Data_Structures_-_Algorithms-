def hasItem_1(adt, item):
    first = 0
    last = len(adt) - 1 
    while first <= last:
        midpoint = (first + last) // 2
        if adt[midpoint] == item:
            return True
        else:
            if item < adt[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return False
