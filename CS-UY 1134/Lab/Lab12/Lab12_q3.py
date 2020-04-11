class EmptyTree(Exception):
    pass

class LinkedBinaryTree:

    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.parent = None
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self

    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(root)

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def subtree_count(self, subtree_root):
        if (subtree_root is None):
            return 0
        else:
            left_count = self.subtree_count(subtree_root.left)
            right_count = self.subtree_count(subtree_root.right)
            return 1 + left_count + right_count


    def sum(self):
        return self.subtree_sum(self.root)

    def subtree_sum(self, subtree_root):
        if (subtree_root is None):
            return 0
        else:
            left_sum = self.subtree_sum(subtree_root.left)
            right_sum = self.subtree_sum(subtree_root.right)
            return subtree_root.data + left_sum + right_sum


    def height(self):
        if(self.is_empty()):
            raise Exception("Height is not defined for an empty tree")
        return self.subtree_height(self.root)

    def subtree_height(self, subtree_root):
        if ((subtree_root.left is None) and (subtree_root.right is None)):
            return 0
        elif ((subtree_root.left is not None) and (subtree_root.right is None)):
            return 1 + self.subtree_height(subtree_root.left)
        elif ((subtree_root.left is None) and (subtree_root.right is not None)):
            return 1 + self.subtree_height(subtree_root.right)
        else:
            left_height = self.subtree_height(subtree_root.left)
            right_height = self.subtree_height(subtree_root.right)
            return 1 + max(left_height, right_height)


    def preorder(self):
        yield from self.subtree_preorder(self.root)

    def subtree_preorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield curr_root
            yield from self.subtree_preorder(curr_root.left)
            yield from self.subtree_preorder(curr_root.right)


    def postorder(self):
        yield from self.subtree_postorder(self.root)

    def subtree_postorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_postorder(curr_root.left)
            yield from self.subtree_postorder(curr_root.right)
            yield curr_root


    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self, curr_root):
        if(curr_root is None):
            pass
        else:
            yield from self.subtree_inorder(curr_root.left)
            yield curr_root
            yield from self.subtree_inorder(curr_root.right)


    def breadth_first(self):
        if (self.is_empty()):
            return
        line = ArrayQueue.ArrayQueue()
        line.enqueue(self.root)
        while (line.is_empty() == False):
            curr_node = line.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                line.enqueue(curr_node.left)
            if (curr_node.right is not None):
                line.enqueue(curr_node.right)


    def __iter__(self):
        for node in self.postorder():
            yield node.data

def same_bst(bst1, bst2):
    if(bst1.size != bst2.size):
        return False
    elem1= bst1.inorder()
    elem2 = bst2.inorder()
    for i in range(bst1.size):
        a = next(elem1).data
        b = next(elem2).data
        print(a, b)
        if(a != b):
            return False
    return True

def search_N_helper(curr_root, N):
    if(curr_root == None):
        return -1
    if(curr_root.data == N):
        return curr_root.data
    elif(curr_root.data < N):
        return max(search_N_helper(curr_root.right, N), curr_root.data)
    elif(curr_root.data > N):
        return search_N_helper(curr_root.left, N)

def search_N(bst, N):
    return search_N_helper(bst.root, N)


a = LinkedBinaryTree.Node(5)
b = LinkedBinaryTree.Node(12)
c = LinkedBinaryTree.Node(25)
d = LinkedBinaryTree.Node(20,None,c)
e = LinkedBinaryTree.Node(10,a,b)
f = LinkedBinaryTree.Node(15,e,d)
tree1 = LinkedBinaryTree(f)
a1 = LinkedBinaryTree.Node(10)
b1 = LinkedBinaryTree.Node(5,None,a1)
c1 = LinkedBinaryTree.Node(12,b1)
e1 = LinkedBinaryTree.Node(25)
d1 = LinkedBinaryTree.Node(20,None,e1)
f1 = LinkedBinaryTree.Node(15,c1,d1)
tree2 = LinkedBinaryTree(f1)

