class Empty(Exception):
    pass

class MaxStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        if(self.is_empty() == True):
            self.data.append((val,val))
        elif(val > self.data[-1][1]):
            self.data.append((val,val))
        else:
            self.data.append((val,self.data[-1][1]))

    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        t=self.data[-1]
        return t[0]

    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        t=self.data.pop()
        return t[0]

    def max(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        t=self.data[-1]
        return t[1]