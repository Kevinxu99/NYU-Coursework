import random
import UnsortedArrayMap

class OpenAddressingHashMap:

    class Item:
        def __init__(self, key, value = None):
            self.key = key
            self.value = value

    def __init__(self, N=64):
        self.N = N
        self.table = [None] * self.N
        self.n = 0

    def __len__(self):
        return self.n

    def __getitem__(self, key):
        i = hash(key) % self.N
        for ind in range(self.N):
            if(self.table[(i+ind)%self.N].key == key):
                return self.table[(i+ind)%self.N].value
        raise KeyError("Key Error:"+str(key))

    def __setitem__(self, key, value):
        i = hash(key) % self.N
        for ind in range(self.N):
            if(self.table[(i+ind)%self.N].key == key):
                self.table[(i+ind)%self.N].value = value
                return
        for ind in range(self.N):
            if(self.table[(i+ind)%self.N] == None):
                self.table[(i+ind)%self.N] = OpenAddressingHashMap.Item(key, value)
                self.n += 1
                if(self.n * 2 > self.N):
                    self.rehash(self.N*2)
                return

    def __delitem__(self, key):
        i = hash(key) % self.N
        for ind in range(self.N):
            if (self.table[(i + ind) % self.N].key == key):
                self.table[(i + ind) % self.N] = None
                self.n -= 1
                if(self.n*8 < self.N):
                    self.rehash(self.N//2)
                return
        raise KeyError("Key Error:" + str(key))

    def __iter__(self):
        for curr_bucket in self.table:
            yield curr_bucket.key

    def rehash(self, new_size):
        old = []
        for item in self.table:
            old.append(item)
        self.table = [None] * new_size
        self.n = 0
        self.N = new_size
        for item in old:
            self[item.key] = item.value
