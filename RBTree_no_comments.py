RED = 0
BLACK = 1

class Node:
    def __init__(self,value):
        self.value=value
        self.left_child=None
        self.right_child=None
        self.parent=None
        self.color=RED

class RBTree:
    def __init__(self):
        self.null_node = Node(None)
        self.null_node.color = BLACK
        self.root = self.null_node
        self.size = 0

    def insert(self,value):
        new_node = Node(value)
        new_node.left_child = self.null_node
        new_node.right_child = self.null_node
        new_node.parent = self.null_node # in case the tree is empty
        new_node.color = RED
        current_node = self.root
        parent_node = self.null_node # to start from the zero and in case the tree is empty 
        while current_node != self.null_node: # check if the tree is empty
            parent_node = current_node # would go down the tree
            if new_node.value < current_node.value: # if the new node value is smaller than the current node value then place it to the left
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child # if the new node value is bigger than the current node value then place it to the right
        new_node.parent = parent_node # set the parent of the new node after it eached to the node that should be the parent of the new node
        if parent_node == self.null_node: # if the tree is empty then the new node is the root
            self.root = new_node
        elif new_node.value < parent_node.value: # if the new node value is smaller than the parent node value then place it to the left
            parent_node.left_child = new_node
        else:
            parent_node.right_child = new_node # else if it's bigger than its parent then place it to the right
        self.fix_RBtree(new_node)
        self.size += 1

    def rotate_left(self,node):
        right_child = node.right_child
        node.right_child = right_child.left_child
        if right_child.left_child != self.null_node:
            right_child.left_child.parent = node
        right_child.parent = node.parent
        if node.parent == self.null_node:
            self.root = right_child
        elif node == node.parent.left_child:
            node.parent.left_child = right_child
        else:
            node.parent.right_child = right_child
        right_child.left_child = node
        node.parent = right_child

    def rotate_right(self,node):
        left_child = node.left_child
        node.left_child = left_child.right_child
        if left_child.right_child != self.null_node:
            left_child.right_child.parent = node
        left_child.parent = node.parent
        if node.parent == self.null_node:
            self.root = left_child
        elif node == node.parent.right_child:
            node.parent.right_child = left_child
        else:
            node.parent.left_child = left_child
        left_child.right_child = node
        node.parent = left_child

    def search(self, value):
        """
        search for a node with a specific value
        """
        node = self.root
        while node != self.null_node:
            if value == node.value:
                return node
            elif value < node.value:
                node = node.left_child
            else:
                node = node.right_child
        return None

    def fix_RBtree(self,node):
        while node.parent.color == RED:
            if node.parent == node.parent.parent.left_child:
                uncle_node=node.parent.parent.right_child
                if uncle_node.color == RED:
                    node.parent.color = BLACK
                    uncle_node.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right_child:
                        node = node.parent
                        self.rotate_left(node) 
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.rotate_right(node.parent.parent)

            else:
                uncle_node=node.parent.parent.left_child
                if uncle_node.color == RED:
                    node.parent.color = BLACK
                    uncle_node.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left_child:
                        node = node.parent
                        self.rotate_right(node)
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.rotate_left(node.parent.parent)
        node.color = BLACK

    def print_height(self):
        def get_height(node):
            if node == self.null_node: 
                return 0
            left_height = get_height(node.left_child) 
            right_height = get_height(node.right_child) 
            return 1 + max(left_height, right_height) 

        print("Tree height: ", get_height(self.root))

    def print_size(self):
        print("Tree size: ", self.size)
