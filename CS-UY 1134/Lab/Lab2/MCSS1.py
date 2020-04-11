import time
import random

class PolyTimer:
    def __init__(self):
        self.start = time.time()

    def elapsed(self):
        return time.time() - self.start

    def reset(self):
        self.start = time.time()

def maxSubsequenceSum1(vals):
    n = len(vals)
    maxSum = 0
    seqStart = 0
    seqEnd = 0

    for i in range(n):
        for j in range(i, n):
            thisSum = 0
            for k in range(i, j + 1):
                thisSum += vals[k]
            if (thisSum > maxSum):
                maxSum = thisSum
                seqStart = i
                seqEnd = j

    return maxSum, seqStart, seqEnd

def main():
    t=PolyTimer()
    nuClicks=0.0
    res=[]
    for i in range(7,13):
        lst=[random.randint(-1000,1000) for j in range(2**i)]
        t.reset()
        result, start, end = maxSubsequenceSum1(lst)
        nuClicks = t.elapsed()
        res.append(nuClicks)
    print (res)

main()
    
