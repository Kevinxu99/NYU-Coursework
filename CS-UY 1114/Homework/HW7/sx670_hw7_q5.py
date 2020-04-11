def encoder(oString):
    count=1
    lst=[]
    for i in range(1,len(oString)):
        if(oString[i]==oString[i-1]):
            count+=1
        else:
            lst.append([oString[i-1],count])
            count=1
    lst.append([oString[len(oString)-1],count])
    return lst

def decoder(lst):
    oString=""
    for i in range(len(lst)):
        oString+=lst[i][0]*lst[i][1]
    return oString
    
def main():
    oString="aadccccaa"
    print(encoder(oString))
    lst=[['a',2],['d',1],['c',4],['a',2]]
    print(decoder(lst))
    
main()
            
