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

def postfix_calculator():
    dict={}
    exp=""
    while(exp != 'done()'):
        exp=input("--> ")
        if(exp != 'done()'):
            num = ArrayStack()
            val = None
            if('=' in exp):
                val=exp[0]
                exp=exp[4:]
            for chr in exp:
                if (chr == ' '):
                    pass
                elif (ord('0') <= ord(chr) <= ord('9')):
                    num.push(int(chr))
                elif (ord('a') <= ord(chr) <= ord('z')):
                    num.push(dict[chr])
                elif (chr in "+-*/"):
                    if(chr == '+'):
                        res = num.pop() + num.pop()
                    if(chr == '-'):
                        num2 = num.pop()
                        num1 = num.pop()
                        res= num1 - num2
                    if(chr == '*'):
                        res = num.pop() * num.pop()
                    if(chr == '/'):
                        num2 = num.pop()
                        num1 = num.pop()
                        res = num1 / num2
                    num.push(res)
            res=num.pop()
            if(val != None):
                dict[val] = res
                print(val)
            else:
                print(res)

postfix_calculator()