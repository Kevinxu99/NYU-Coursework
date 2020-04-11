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

def create_expression_tree_helper(prefix_exp, start_pos):
    if(prefix_exp[start_pos] in '+-*/'):
        curr_size = 1
        expression_tree = LinkedBinaryTree(LinkedBinaryTree.Node(prefix_exp[start_pos]))
        if(prefix_exp[start_pos+1] not in '+-*/'):
            left_subtree = (LinkedBinaryTree.Node(int(prefix_exp[start_pos+1])), 1)
            expression_tree.root.left = left_subtree[0]
            curr_size += 1
        else:
            left_subtree = create_expression_tree_helper(prefix_exp,start_pos+1)
            expression_tree.root.left = left_subtree[0].root
            curr_size += left_subtree[1]
        right_ind = start_pos+curr_size
        if(right_ind < len(prefix_exp)):
            if(prefix_exp[right_ind] not in '+-*/'):
                right_subtree = (LinkedBinaryTree.Node(int(prefix_exp[right_ind])),1)
                expression_tree.root.right = right_subtree[0]
                curr_size += 1
            else:
                right_subtree = create_expression_tree_helper(prefix_exp,right_ind)
                expression_tree.root.right = right_subtree[0].root
                curr_size += right_subtree[1]
        return (expression_tree, curr_size)



def create_expression_tree(prefix_exp_str):
    prefix_exp_lst = prefix_exp_str.strip().split()
    return create_expression_tree_helper(prefix_exp_lst,0)[0]

def prefix_to_postfix(prefix_exp_str):
    expression_tree = create_expression_tree(prefix_exp_str)
    postfix_lst = []
    for item in expression_tree.postorder():
        postfix_lst.append(str(item.data))
    return ' '.join(postfix_lst)

