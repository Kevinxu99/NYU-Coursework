class BoostQueue:
    INITIAL_CAPACITY = 5

    def __init__(self):
        self.data = [None] * BoostQueue.INITIAL_CAPACITY
        self.front_ind = 0
        self.number_of_elems = 0

    def __len__(self):
        return self.number_of_elems

    def is_empty(self):
        return (len(self) == 0)

    def enqueue(self, item):
        if (self.number_of_elems == len(self.data)):
            self.resize(2 * len(self.data))
        end_ind = (self.front_ind + self.number_of_elems) % len(self.data)
        self.data[end_ind] = item
        self.number_of_elems += 1

    def dequeue(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.number_of_elems -= 1
        if (self.number_of_elems < (len(self.data) // 4)):
            self.resize(len(self.data) // 2)
        return value

    def first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        return self.data[self.front_ind]

    def boost(self,k):
        value=self.dequeue()
        print(value)
        if(k >= self.number_of_elems):
            self.front_ind = (self.front_ind + len(self.data) - 1) % len(self.data)
            self.data[self.front_ind] = value
            self.number_of_elems += 1
        else:
            end_ind=(self.front_ind+self.number_of_elems)%len(self.data)
            boost_ind=(end_ind+len(self.data)-k) % len(self.data)
            for i in range(0,k):
                ind = (end_ind - i + len(self.data)) % len(self.data)
                self.data[ind]=self.data[(ind+len(self.data)-1)%len(self.data)]
            self.data[boost_ind]=value
            self.number_of_elems += 1


    def resize(self, new_capacity):
        new_data = [None] * new_capacity
        old_ind = self.front_ind
        for new_ind in range(self.number_of_elems):
            new_data[new_ind] = self.data[old_ind]
            old_ind = (old_ind + 1) % len(self.data)
        self.data = new_data
        self.front_ind = 0
