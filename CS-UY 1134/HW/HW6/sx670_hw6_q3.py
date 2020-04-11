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

class CompactString:

    def __init__(self, orig_str):
        self.data = DoublyLinkedList()
        prev_item = orig_str[0]
        item_count=0
        for item in orig_str:
            if item == prev_item:
                item_count += 1
            else:
                self.data.add_last((prev_item, item_count))
                prev_item = item
                item_count = 1
        self.data.add_last((prev_item, item_count))

    def __add__(self, other):
        res = CompactString(repr(self))
        last_chr = self.data.last_node()
        first_chr = other.data.first_node()
        if last_chr.data[0] == first_chr.data[0]:
            res.data.last_node().data = (last_chr.data[0] ,last_chr.data[1] + first_chr.data[1])
            first_chr = first_chr.next
            while not first_chr == other.data.trailer:
                res.data.add_last(first_chr.data)
                first_chr = first_chr.next
        else:
            while not first_chr == other.data.trailer:
                res.data.add_last(first_chr.data)
                first_chr = first_chr.next
        return res

    def __lt__(self, other):
        node1 = self.data.first_node()
        node2 = other.data.first_node()
        while (node1 != self.data.trailer and node2 != other.data.trailer):
            if(ord(node1.data[0]) < ord(node2.data[0])):
                return True
            elif(ord(node1.data[0]) > ord(node2.data[0])):
                return False
            else:
                if(node1.data[1] > node2.data[1]):
                    if(ord(node1.data[0]) < ord(node2.next.data[0])):
                        return True
                    else:
                        return False
                elif(node1.data[1] < node2.data[1]):
                    if (ord(node1.next.data[0]) < ord(node2.data[0])):
                        return True
                    else:
                        return False
            node1 = node1.next
            node2 = node2.next
        if(self.data.size < other.data.size):
            return True
        else:
            return False


    def __le__(self, other):
        node1 = self.data.first_node()
        node2 = other.data.first_node()
        while (node1 != self.data.trailer and node2 != other.data.trailer):
            if (ord(node1.data[0]) < ord(node2.data[0])):
                return True
            elif (ord(node1.data[0]) > ord(node2.data[0])):
                return False
            else:
                if (node1.data[1] > node2.data[1]):
                    if (ord(node1.data[0]) < ord(node2.next.data[0])):
                        return True
                    else:
                        return False
                elif (node1.data[1] < node2.data[1]):
                    if (ord(node1.next.data[0]) < ord(node2.data[0])):
                        return True
                    else:
                        return False
            node1 = node1.next
            node2 = node2.next
        if (self.data.size > other.data.size):
            return False
        else:
            return True

    def __gt__(self, other):
        node1 = self.data.first_node()
        node2 = other.data.first_node()
        while (node1 != self.data.trailer and node2 != other.data.trailer):
            if (ord(node1.data[0]) > ord(node2.data[0])):
                return True
            elif (ord(node1.data[0]) < ord(node2.data[0])):
                return False
            else:
                if (node1.data[1] > node2.data[1]):
                    if (ord(node1.data[0]) > ord(node2.next.data[0])):
                        return True
                    else:
                        return False
                elif (node1.data[1] < node2.data[1]):
                    if (ord(node1.next.data[0]) > ord(node2.data[0])):
                        return True
                    else:
                        return False
            node1 = node1.next
            node2 = node2.next
        if (self.data.size > other.data.size):
            return True
        else:
            return False

    def __ge__(self, other):
        node1 = self.data.first_node()
        node2 = other.data.first_node()
        while (node1 != self.data.trailer and node2 != other.data.trailer):
            if (ord(node1.data[0]) > ord(node2.data[0])):
                return True
            elif (ord(node1.data[0]) < ord(node2.data[0])):
                return False
            else:
                if (node1.data[1] > node2.data[1]):
                    if (ord(node1.data[0]) > ord(node2.next.data[0])):
                        return True
                    else:
                        return False
                elif (node1.data[1] < node2.data[1]):
                    if (ord(node1.next.data[0]) > ord(node2.data[0])):
                        return True
                    else:
                        return False
            node1 = node1.next
            node2 = node2.next
        if (self.data.size < other.data.size):
            return False
        else:
            return True

    def __repr__(self):
        stri = ''
        for item in self.data:
            stri = stri + item[0]*item[1]
        return stri