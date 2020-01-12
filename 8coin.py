"""Problem: We have 8 coins, one of which is ingenuine and lighter. The other 7 are legit. I'm trying to find which is fake"""

import numpy as np
a=[1,1,1,0,1,1,1,1]
a=np.array(a)

#first split
aL=np.split(a,2)[0]
aR=np.split(a,2)[1]

# compare first, second split

if np.sum(aL)>np.sum(aR):
    aRL=np.split(aR,2)[0]
    aRR=np.split(aR,2)[1]

#compare second, third split

    if np.sum(aRL)>np.sum(aRR):
        aRRL=np.split(aRR,2)[0]
        aRRR=np.split(aRR,2)[1]

# compare third, find ingenuine

        if np.sum(aRRL)>np.sum(aRRR):
            print('Last coin is fake')
        else:
            print('7th coin is fake')
    else:
        aRLL=np.split(aRL,2)[0]
        aRLR=np.split(aRL,2)[1]

        if np.sum(aRLL)>np.sum(aRLR):
            print('6th coin is fake')
        else:
            print('5th coin is fake')
else:
    aLL=np.split(aL,2)[0]
    aLR=np.split(aL,2)[1]


    if np.sum(aLL)>np.sum(aLR):
        aLRL=np.split(aLR,2)[0]
        aLRR=np.split(aLR,2)[1]

        if np.sum(aLRL)>np.sum(aLRR):
            print('4th coin is fake')
        else:
            print('3rd coin is fake')
    else:
        aLLL=np.split(aLL,2)[0]
        aLLR=np.split(aLL,2)[1]
        if np.sum(aLLL)>np.sum(aLLR):
            print('2nd coin is fake')
        else:
            print('1st coin is fake')
