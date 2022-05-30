
    def swap_two_elements(alist, pos1, pos2):
        temp = alist[pos1]
        alist[pos1] = alist[pos2]
        alist[pos2] = temp
        return alist[pos1], alist[pos2]


    def swap_to_elements(alist, pos1, pos2):
        alist[pos1], alist[pos2] = alist[pos2], alist[pos1]


    def bubbleSort(alist):
        for passnum in range(len(alist)-1, 0, -1):
            for i in range(passnum):
                #print('still working')
                if alist[i] > alist[i+1]:
                    swap_to_elements(alist, i, i+1)


    def bubbleSortSmart(alist):
        stillWorking = True
        passnum = len(alist) - 1
        while passnum > 0 and stillWorking:
            stillWorking = False
            for i in range(passnum):
                #print('still working')
                if alist[i] > alist[i+1]:
                    swap_two_elements(alist, i, i+1)
                    stillWorking = True
            passnum -= 1


    def selectionSort(alist):
        for fillslot in range(len(alist)-1, 0, -1):
            positionOfMax = 0
            for location in range(1, fillslot+1):
                if alist[location] > alist[positionOfMax]:
                    positionOfMax = location

            swap_two_elements(alist, fillslot, positionOfMax)


    def insertionSort(alist):
        for index in range(1,len(alist)):
            currentvalue = alist[index]
            position = index
            while position > 0 and alist[position-1] > currentvalue:
                alist[position] = alist[position-1]
                position -= 1

            alist[position] = currentvalue


    def shellSort(alist):
        sublistcount = len(alist) // 2
        while sublistcount > 0:
            for startposition in range(sublistcount):
                gapInsertionSort(alist, startposition, sublistcount)

            sublistcount = sublistcount // 2

    def gapInsertionSort(alist,start,gap):
        for i in range(start+gap, len(alist), gap):
            currentvalue = alist[i]
            position = i

            while position>=gap and alist[position-gap]>currentvalue:
                alist[position]=alist[position-gap]
                position = position-gap

            alist[position]=currentvalue


    def mergeSort(alist):
        print("Splitting ", alist)
        if len(alist) > 1:
            mid = len(alist) // 2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]

            mergeSort(lefthalf)
            mergeSort(righthalf)

            i = 0
            j = 0
            k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] <= righthalf[j]:
                    alist[k] = lefthalf[i]
                    i = i+1
                else:
                    alist[k] = righthalf[j]
                    j = j+1
                k = k+1

            while i < len(lefthalf):
                alist[k] = lefthalf[i]
                i = i+1
                k = k+1

            while j < len(righthalf):
                alist[k] = righthalf[j]
                j = j+1
                k = k+1
        print("Merging ",alist)

