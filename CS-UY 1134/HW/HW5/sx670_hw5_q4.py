class Empty(Exception):
    pass


class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data.pop()


class Queue:
    def __init__(self):
        self.inputStack = ArrayStack()
        self.outputStack = ArrayStack()
        self.num_of_elems = 0

    def is_empty(self):
        return (self.num_of_elems == 0)

    def enqueue(self, val):
        self.inputStack.push(val)
        self.num_of_elems += 1

    def dequeue(self):
        if (self.is_empty()):
            raise Empty("Queue is empty")
        if (self.outputStack.is_empty()):
            while (self.inputStack.is_empty() == False):
                self.outputStack.push(self.inputStack.pop())
        self.num_of_elems -= 1
        return self.outputStack.pop()

    def first(self):
        if (self.is_empty()):
            raise Empty("Queue is empty")
        if (self.outputStack.is_empty()):
            while (self.inputStack.is_empty()==False):
                self.outputStack.push(self.inputStack.pop())
        return self.outputStack.top()