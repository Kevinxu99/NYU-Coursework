def sum_column(filename):
    f=open(filename,"r")
    s=0
    for line in f:
        s+=int(line)
    return s

def main():
    print(sum_column("Lab10_p3.txt"))

main()
