class BinaryPositiveInteger:
    def __init__(self,num):
        self.binary=""
        i=0
        while((2**i)<=num):
            i+=1
        i-=1
        while(i>=0):
            if(num>=2**i):
                self.binary=self.binary+'1'
                num-=(2**i)
            else:
                self.binary=self.binary+'0'
            i-=1

    def __add__(self,other):
        l1=len(self.binary)
        l2=len(other.binary)
        if(l1>l2):
            other.binary='0'*(l1-l2)+other.binary
            l=l1
        else:
            self.binary='0'*(l2-l1)+self.binary
            l=l2
        t=0
        Sum=""
        for i in range(1,l+1):
            if(t==1):
                if(self.binary[l-i]=='0' and other.binary[l-i]=='0'):
                    Sum='1'+Sum
                    t=0
                elif(self.binary[l-i]=='1' and other.binary[l-i]=='1'):
                    Sum='1'+Sum
                    t=1
                else:
                    Sum='0'+Sum
                    t=1
            else:
                if(self.binary[l-i]=='0' and other.binary[l-i]=='0'):
                    Sum='0'+Sum
                    t=0
                elif(self.binary[l-i]=='1' and other.binary[l-i]=='1'):
                    Sum='0'+Sum
                    t=1
                else:
                    Sum='1'+Sum
                    t=0
        if(t==1):
            Sum='1'+Sum
        s=BinaryPositiveInteger(0)
        s.binary=Sum
        return repr(s)
                           
    def __lt__(self,other):
        l1=len(self.binary)
        l2=len(other.binary)
        if(l1<l2):
            return True
        if(l2>l1):
            return False
        for i in range(1,l1):
            if(self.binary[i]=='0' and other.binary[i]=='1'):
                return True
        return False

    def __mul__(self,other):
        l1=len(self.binary)
        l2=len(other.binary)
        p=BinaryPositiveInteger(0)
        s=BinaryPositiveInteger(0)
        s.binary=''
        for i in range(1,l2+1):
            if(other.binary[l2-i]=='1'):
                s.binary=self.binary
                s.binary=s.binary+'0'*(i-1)
                p.binary=p+s
                p.binary=p.binary[2:]
        return repr(p)
                   
    def is_power_of_2(self):
        for i in range(1,len(self.binary)):
            if(self.binary[i]=='1'):
                return False
        return True

    def largest_power_of_2(self):
        return 2**(len(self.binary)-1)

    def __repr__(self):
        return '0b'+self.binary

def main():
    n1=BinaryPositiveInteger(13)
    print(repr(n1))
    n2=BinaryPositiveInteger(25)
    print(repr(n2))
    print(n1.is_power_of_2())
    print(n1.largest_power_of_2())
    print(n1<n2)
    print(n1+n2)
    print(n1*n2)

main()
