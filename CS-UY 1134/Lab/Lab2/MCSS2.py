import time
import random

class PolyTimer:
    def __init__(self):
        self.start = time.time()

    def elapsed(self):
        return time.time() - self.start

    def reset(self):
        self.start = time.time()

def maxSubsequenceSum2(vals):
    n = len(vals)
    maxSum = 0
    seqStart = 0
    seqEnd = 0

    for i in range(n):
        thisSum = 0
        for j in range(i, n):
            thisSum += vals[j]
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
        result, start, end = maxSubsequenceSum2(lst)
        nuClicks = t.elapsed()
        res.append(nuClicks)
    print (res)
    f=open("MCSS2.csv","w")
    for val in res:
        f.write(str(val)+"\n")
    f.close()

main()
    
