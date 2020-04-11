class Poly:
    def __init__(self,lst):
        self.coef=lst
        self.p=""
        for i in range(len(self.coef)-1,-1,-1):
            if (i==len(self.coef)-1):
                self.p=self.p+str(self.coef[i])
                if(i==1):
                    self.p=self.p+'x'
                if(i>1):
                    self.p=self.p+'x^'+str(i)
            elif (self.coef[i]==1 and i!=0):
                self.p=self.p+'+'
                if(i==1):
                    self.p=self.p+'x'
                if(i>1):
                    self.p=self.p+'x^'+str(i)
            elif (self.coef[i]>0):
                self.p=self.p+'+'+str(self.coef[i])
                if(i==1):
                    self.p=self.p+'x'
                if(i>1):
                    self.p=self.p+'x^'+str(i)
            elif (self.coef[i]<0):
                self.p=self.p+str(self.coef[i])
                if(i==1):
                    self.p=self.p+'x'
                if(i>1):
                    self.p=self.p+'x^'+str(i)
                    
    def eval(self,val):
        r=0
        for i in range(len(self.coef)):
            r+=(self.coef[i]*(val**i))
        return r

    def __add__(self,other):
        if(len(self.coef)>=len(other.coef)):
            lst1=self.coef.copy()
            lst2=other.coef.copy()
        else:
            lst1=other.coef.copy()
            lst2=self.coef.copy()
        for i in range(len(lst2)):
            lst1[i]+=lst2[i]
        while(lst1[len(lst1)-1]==0):
            lst1.pop()
        a=Poly(lst1)
        return a

    def __mul__(self,other):
        pd=[0 for i in range(len(self.coef)+len(other.coef)-1)]
        for i in range(len(self.coef)):
            for j in range(len(other.coef)):
                #print(pd)
                pd[i+j]+=(self.coef[i]*other.coef[j])
        while(pd[len(pd)-1]==0):
            pd.pop()
        #print (pd)
        m=Poly(pd)
        return m

    def derive(self):
        for i in range(1,len(self.coef)-1):
            self.coef[i]=self.coef[i]*i
        self.coef=self.coef[1:]
        return Poly(self.coef)
    
    def __repr__(self):
        if self.p == "":
            return 'p(x)=0'
        else:
            return 'p(x)='+self.p

def main():
    p1=Poly([0,1,5])
    p2=Poly([0,1,3,0,0,0,0,0,2])
    print(p1)
    print(p2)
    print(p1.eval(1))
    print(p1+p2)
    print(p1*p2)
    print(p1.derive())
    

main()
