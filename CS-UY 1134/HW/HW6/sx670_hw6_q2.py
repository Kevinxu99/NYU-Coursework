class Empty(Exception):
    pass

class DoublyLinkedList:
    class Node:
        def __init__(self, data=None, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

        def disconnect(self):
            self.data = None
            self.prev = None
            self.next = None


    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def first_node(self):
        if(self.is_empty()):
          raise Empty("List is empty")
        return self.header.next

    def last_node(self):
        if(self.is_empty()):
          raise Empty("List is empty")
        return self.trailer.prev

    def add_after(self, node, data):
        prev = node
        succ = node.next
        new_node = DoublyLinkedList.Node(data, prev, succ)
        prev.next = new_node
        succ.prev = new_node
        self.size += 1
        return new_node

    def add_first(self, data):
        return self.add_after(self.header, data)

    def add_last(self, data):
        return self.add_after(self.trailer.prev, data)

    def add_before(self, node, data):
        return self.add_after(node.prev, data)

    def delete_node(self, node):
        pred = node.prev
        succ = node.next
        pred.next = succ
        succ.prev = pred
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def delete_first(self):
        if (self.is_empty()):
            raise Empty("List is empty")
        self.delete_node(self.first_node())

    def delete_last(self):
        if (self.is_empty()):
            raise Empty("List is empty")
        self.delete_node(self.last_node())

    def __iter__(self):
        if (self.is_empty()):
            return
        cursor = self.first_node()
        while cursor is not self.trailer:
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return "[" + " <--> ".join([str(item) for item in self]) + "]"

class Integer:

    def __init__(self, num_str):
        self.data = DoublyLinkedList()
        for val in num_str:
            self.data.add_before(self.data.trailer, int(val))

    def __add__(self, other):
        if(self.data.size > other.data.size):
            res = Integer('0'*(self.data.size+1))
        else:
            res = Integer('0'*(other.data.size+1))
        node1 = self.data.last_node()
        node2 = other.data.last_node()
        node3 = res.data.last_node()
        while not (node1 == self.data.header and node2 == other.data.header):
            if(node1 == self.data.header):
                val1 = 0
            else:
                val1 = node1.data
            if(node2 == other.data.header):
                val2 = 0
            else:
                val2 = node2.data
            val = node3.data+val1+val2
            node3.data = val%10
            if(val >= 10):
                node3.prev.data = 1
            if(node1!=self.data.header):
                node1=node1.prev
            if(node2!=other.data.header):
                node2=node2.prev
            node3 = node3.prev
        while(res.data.first_node().data == 0):
           res.data.delete_first()
        return res


    def __repr__(self):
        return ''.join([str(item) for item in self.data])