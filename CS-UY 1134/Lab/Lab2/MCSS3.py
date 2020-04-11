import time
import random
import csv

class PolyTimer:
    def __init__(self):
        self.start = time.time()

    def elapsed(self):
        return time.time() - self.start

    def reset(self):
        self.start = time.time()

def maxSubsequenceSum3(vals):
    n = len(vals)
    thisSum = 0
    maxSum = 0
    
    i = 0
    seqStart = 0
    seqEnd = 0
    for j in range(n):
        thisSum += vals[j]
        if (thisSum > maxSum):
            maxSum = thisSum
            seqStart = i
            seqEnd = j
        elif (thisSum < 0):
            i = j + 1
            thisSum = 0

    return maxSum, seqStart, seqEnd

def main():
    t=PolyTimer()
    nuClicks=0.0
    res=[]
    for i in range(7,13):
        lst=[random.randint(-1000,1000) for j in range(2**i)]
        t.reset()
        result, start, end = maxSubsequenceSum3(lst)
        nuClicks = t.elapsed()
        res.append(nuClicks)
    print(res)

main()
    
