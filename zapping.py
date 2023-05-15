"""
SUMMARY OF THE PROBLEM:
Ioannis wants to ocassionaly switch all of his TV's to the same channel; channel doesn't matter. 
He only has 1 remote, which has only 1 next button to change 1 tv's channel to next 
--> correspondence to incrementing 1 value in the list by 1 at a time?
When he reaches the last channel (the max channel number), roll over to 1; note all TV's have same channels in same order

Cannot press next twice for same TV, have to press next in another intermediate. This basically means you can't press next consecutively 
for the same TV

Find minimum # of channel changes needed to synchronize the TV's. You must determine best channel to flip to (use metric of distance?)

No concrete efficiency requirement (needs to run within 10 minutes)

EXAMPLE WALKTHROUGHS (index starts at 1)

EX 1: # channels = 5, [3 1 3 3] --> output = 6; [4 4 4 4]; pressNextSeq = 1, 2, 3, 2, 4, 2

3 1 3 3 --> 4 1 3 3 --> 4 2 3 3 --> 4 2 4 3 --> 4 3 4 3 --> 4 3 4 4 --> 4 4 4 4 (DONE)

EX 2: # channels = 6, [4,3,1,4,5] --> output = 8; [5,5,5,5,5]

4, 3, 1, 4, 5 

TOTAL DISTANCE TO 1 --> (4 - 1) + (3 - 1) + (1 - 1) + (4 - 1) + (5 - 1) = 3 + 2 + 0 + 3 + 4 = 12
TOTAL DISTANCE TO 2 --> (4 - 2) + (3 - 2) + (2 - 1) + (4 - 2) + (5 - 2) = 2 + 1 + 1 + 2 + 3 = 9
TOTAL DISTANCE TO 3 --> (4 - 3) + (3 - 3) + (3 - 1) + (4 - 3) + (5 - 3) = 1 + 0 + 2 + 1 + 2 = 6
TOTAL DISTANCE TO 4 --> (4 - 4) + (4 - 3) + (4 - 1) + (4 - 4) + (5 - 4) = 0 + 1 + 3 + 0 + 1 = 5
TOTAL DISTANCE TO 5 --> (5 - 4) + (5 - 3) + (5 - 1) + (5 - 4) + (5 - 5) = 1 + 2 + 4 + 1 + 0 = 7
Smallest distances heuristic doesn't work :(

4 3 1 4 5 -->(1) 5 3 1 4 5 -->(3) 5 3 2 4 5 -->(2) 5 4 2 4 5 -->(3) 5 4 3 4 5 -->(2) 5 5 3 4 5 -->(3) 5 5 4 4 5 -->(4) 5 5 4 5 5 -->(3) 5 5 5 5 5

Given sequence: 1 3 2 3 2 3 4 3

Idea may be to prioritize lower-valued number, alternations also prioritize 


PSEUDOCODE:

increment the first number, if it is not the max number
increment the second number
alternate incrementing second and third number until they equal first number
rinse and repeat?
This method only passes 1 test case and is not correct

What if we sorted in ascending order?
increment last elem if it's not strictly greater than left number
increment smallest number
Use a loop to find next number to increment during alternation
but what if we have multiple tv's set to last channel?



"""

import math
import re
class Zapping(object):

    def eval(self, list2):
        tokens2 = list2.split()
        list3 = list(map(int, tokens2))
        # list3[0] has the number of channels, list3[1], list3[2], ... denote
        # the channel each TV currently shows
        # your code here, value is the answer
        value = -1 # sanity check

        maxChannel = list3[0]; # for readability
        numTV = len(list3) - 1 # number of tv's, indexed starting at 1

        """
        # Below is some experimentation...

        if list3[1] < numChannels:
            list3[1] += 1
            value += 1
        
        currLeft = 1
        while currLeft < numTV:
            if list3[currLeft] != list3[1]:
                while list3[currLeft] < list3[1]:
                    list3[currLeft] += 1
                    list3[currLeft+1] += 1
                    value += 2
                if list3[currLeft] > numChannels:
                    list3[currLeft] = 1
                if list3[currLeft+1] > numChannels:
                    list3[currLeft+1] = 1
            currLeft += 1
        

         # rearrange TV's in ascending order according to initial channel
        tvSort = copy.deepcopy(list3[1:])
        tvSort.sort()
        if tvSort[-1] == tvSort[-2] and tvSort != maxChannel:
            tvSort[-1] += 1
        
        currRight = tvSort[1]
        currLeft = tvSort[0]
        recentIncrement = False # true if currLeft was most recently incremented
        while currRight < numTV: # every element in list must now equal last elem
            if currRight == tvSort[-1]:
                currRight += 1
            elif not recentIncrement:
                if currLeft == tvSort[-1]:
                    currLeft += 1
                else:
                    tvSort[currLeft] += 1
                    value += 1
            elif recentIncrement:
                if currRight == tvSort[-1]:
                    currRight += 1
                else:
                    tvSort[currRight] += 1
                    value += 1   
        """

        sortedTV = list3[1:].copy() # size = numTV
        sortedTV.sort()

        # instead of subtracting go the long way round...
        median = numTV // 2 # index of median value



        return value

if __name__ == '__main__':
    calc = Zapping()
    calc.eval()