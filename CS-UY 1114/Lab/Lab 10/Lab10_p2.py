import random
def write_random_numbers(filename,n):
    f=open(filename,"w")
    for i in range (n):
        a=random.randint(1,100)
        f.write(str(a)+"\n")

def main():
    write_random_numbers("lab11_q2.txt",5)

main()
