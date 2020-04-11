import ctypes
def make_array(n):
    return (n*ctypes.py_object)()

class MyString:
    def __init__(self,initial_str=""):
        self.n=0
        for curr in initial_str:
            self.n+=1
        self.data=make_array(self.n)
        for i in range(self.n):
            self.data[i]=initial_str[i]

    def __len__(self):
        return self.n

    def __iter__(self):
        for i in range(self.n):
            yield self.data[i]

    def get_item(self,ind):
        if(ind>=self.n or ind<(-self.n)):
            raise IndexError("invalid index")
        if(ind<0):
            ind=self.n+ind
        return self.data[ind]

    def __add__(self,new_str):
        other=MyString(new_str)
        sum_data=make_array(self.n+other.n)
        for i in range(self.n):
            sum_data[i]=self.data[i]
        for i in range(self.n,self.n+other.n):
            sum_data[i]=other.data[i-self.n]
        return "".join(sum_data)

    def __radd__(self,new_str):
        other = MyString(new_str)
        sum_data = make_array(self.n + other.n)
        for i in range(other.n):
            sum_data[i] = other.data[i]
        for i in range(other.n, self.n + other.n):
            sum_data[i] = self.data[i - other.n]
        return "".join(sum_data)

    def upper(self):
        for i in range(self.n):
            if(self.data[i]>='a' and self.data[i]<='z'):
                self.data[i]=chr(ord(self.data[i])-32)

    def __repr__(self):
        return "".join(self.data)