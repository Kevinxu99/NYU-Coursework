import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class MyList:
    def __init__(self):
        self.data = make_array(1)
        self.n = 0
        self.capacity = 1

    def append(self, val):
        if(self.n == self.capacity):
            self.resize(2*self.capacity)
        self.data[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_arr = make_array(new_size)
        for i in range(self.n):
            new_arr[i] = self.data[i]
        self.data = new_arr
        self.capacity = new_size

    def __len__(self):
        return self.n

    def __getitem__(self, ind):
        if isinstance(ind, slice):
            return [self[i] for i in range(*ind.indices(len(self)))]
        elif isinstance(ind, int):
            if (not(-(self.n) <=ind <= (self.n - 1))):
                raise IndexError("invalid index")
            if(ind<0):
                return self.data[len(self)+ind]
            return self.data[ind]

    def __setitem__(self, ind, val):
        if (not(-(self.n) <= ind <= (self.n - 1))):
            raise IndexError("invalid index")
        if(ind<0):
            self.data[len(self)+ind] = val
        else:
            self.data[ind] = val

    def __iter__(self):
        for i in range(self.n):
            yield self.data[i]

    def extend(self, iterable_collection):
        for elem in iterable_collection:
            self.append(elem)

    def insert(self, index, val):
        if(index > (len(self)-1) or index< -(len(self))):
            raise IndexError("invalid index")
        else:
            if(index<0):
                index=len(self)+index
            new_arr=make_array(len(self))
            for i in range(len(self)):
                new_arr[i]=self.data[i]
            self.data[index]=val
            for i in range(index+1,len(self)):
                self.data[i]=new_arr[i-1]
            self.append(new_arr[len(self)-1])

    def pop(self):
        pop_item=self.data[len(self)-1]
        self.n-=1
        if(self.n<self.capacity//4):
            self.resize(self.capacity//2)
        return pop_item

    def __add__(self,other):
        res=MyList()
        res.extend(iter(self))
        res.extend(iter(other))
        return res

    def __iadd__(self,other):
        self.extend(iter(other))
        return self

    def __mul__(self,n):
        p=MyList()
        for i in range(0,n):
            p.extend(iter(self))
        return p

    def __rmul__(self,n):
        return self * n

    def __repr__(self):
        str_lst=MyList()
        for i in self:
            str_lst.append(str(i))
        return "["+",".join(str_lst)+"]"