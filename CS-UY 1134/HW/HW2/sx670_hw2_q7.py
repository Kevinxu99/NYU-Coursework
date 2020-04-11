def findChange(lst01):
    left=0
    right=len(lst01)-1
    while(left<right):
        mid=(left+right)//2
        if(lst01[mid]==0 and lst01[mid+1]==1):
            return mid+1
        if(lst01[mid]==0):
            left=mid
        if(lst01[mid]==1):
            right=mid


