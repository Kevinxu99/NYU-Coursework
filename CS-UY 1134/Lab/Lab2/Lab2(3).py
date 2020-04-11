def move_zeroes(nums):
    n=nums.count(0)
    for i in range (n):
        nums.remove(0)
    for i in range(n):
        nums.append(0)

def main():
    nums=[0,1,3,0,13]
    move_zeroes(nums)
    print(nums)

main()
    
        
