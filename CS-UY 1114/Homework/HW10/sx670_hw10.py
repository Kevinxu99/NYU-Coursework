def MTASystem(train,filename):
    f=open(filename,"r")
    header=f.readline().strip().split(",")
    for stop in f:
        stop_info=stop.strip().split(",")
        line=stop_info[0][0]
        if(line not in train):
            train[line]=[]
        if(stop_info[0][-1]!='N' and stop_info[0][-1]!='S'):
            train[line].append(stop_info[2])
            
def trainstops(line,train):
    print(line,"line: ",end="")
    for stop in train[line]:
        print(stop,", ",sep="",end="")
    print("\n")
    
def main():
    train={}
    MTASystem(train,"hw10 - mta train stop data.csv")
    while(1):
        n=input("Please enter a train line, or 'done' to stop: ")
        if(n=='done'):
            break
        trainstops(n,train)

main()
