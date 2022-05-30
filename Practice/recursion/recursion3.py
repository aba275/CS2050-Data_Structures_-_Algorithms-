def recMC(coinValueList,change, knownResults):
    #print('making change for: ', str(change))
    minCoins = change
    if change in coinValueList:
        #print('returning 1 since change is same as coin')
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            #print(' 1 = ', str(i))
            numCoins = 1 + recMC(coinValueList, change-i, knownResults)
            if numCoins < minCoins:
                #print('     *** numCoins = ', str(numCoins), '<', str(minCoins), '=minCoins')
                minCoins = numCoins
                knownResults[change] = minCoins
    #print('returning minCoins = ', minCoins())
    return minCoins

print(recMC([1,5,10,25], 63, [0]*64))