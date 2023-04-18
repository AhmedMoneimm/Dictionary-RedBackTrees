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
    """
    the null node is created and the color is set to black
    """
    def __init__(self):
        self.null_node = Node(None)
        self.null_node.color = BLACK
        self.root = self.null_node
        self.size = 0
#__________________________________________________________________________________________________________________________________________________
    def insert(self,value):
        """
        the new node is created and the color is set to red
        """
        new_node = Node(value)

        new_node.left_child = self.null_node
        new_node.right_child = self.null_node
        new_node.parent = self.null_node # in case the tree is empty
        new_node.color = RED

        """
        while loop is made to reach the node that should be the parent of the new node
        """
        current_node = self.root
        parent_node = self.null_node # to start from the zero and in case the tree is empty 
        
        while current_node != self.null_node: # check if the tree is empty
            parent_node = current_node # would go down the tree
            if new_node.value < current_node.value: # if the new node value is smaller than the current node value then place it to the left
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child # if the new node value is bigger than the current node value then place it to the right

        new_node.parent = parent_node # set the parent of the new node after it eached to the node that should be the parent of the new node

        """
        the if conditional is made to place the new node in the tree under its parent we found in the while loop
        """
        if parent_node == self.null_node: # if the tree is empty then the new node is the root
            self.root = new_node
        elif new_node.value < parent_node.value: # if the new node value is smaller than the parent node value then place it to the left
            parent_node.left_child = new_node
        else:
            parent_node.right_child = new_node # else if it's bigger than its parent then place it to the right

        """
        the tree right now has some violations for the RBTree properties
        it needs to be fixed
        """
        self.fix_RBtree(new_node)

        """
        the size of the tree is increased by 1
        """
        self.size += 1
#__________________________________________________________________________________________________________________________________________________
    def rotate_left(self,node):
        """
        the right child of the node becomes the parent of the node
        """
        right_child = node.right_child # set the right child of the node to a variable 
        node.right_child = right_child.left_child # set the left child of the right child of the node to be the right child of the current node

        if right_child.left_child != self.null_node:
            right_child.left_child.parent = node

        right_child.parent = node.parent # set the parent of the right child of the node to be the parent of the current node

        if node.parent == self.null_node:
            self.root = right_child # if the current node is the root then set the right child to be the new root
        elif node == node.parent.left_child:
            node.parent.left_child = right_child # if the current node is the left child of its parent then set the right child of the current node to be the new left child of the parent
        else:
            node.parent.right_child = right_child # else set the right child of the current node to be the new right child of the parent

        right_child.left_child = node # set the current node to be the left child of the right child of the node
        node.parent = right_child # set the parent of the current node to be the right child of the node
#__________________________________________________________________________________________________________________________________________________
    def rotate_right(self,node):
        """
        the left child of the node becomes the parent of the node
        """
        left_child = node.left_child # set the left child of the node to a variable
        node.left_child = left_child.right_child # set the right child of the left child of the node to be the left child of the current node

        if left_child.right_child != self.null_node:
            left_child.right_child.parent = node

        left_child.parent = node.parent # set the parent of the left child of the node to be the parent of the current node
        
        if node.parent == self.null_node:
            self.root = left_child # if the current node is the root then set the left child to be the new root
        elif node == node.parent.right_child:
            node.parent.right_child = left_child # if the current node is the right child of its parent then set the left child of the current node to be the new right child of the parent
        else:
            node.parent.left_child = left_child # else set the left child of the current node to be the new left child of the parent
        
        left_child.right_child = node # set the current node to be the right child of the left child of the node
        node.parent = left_child # set the parent of the current node to be the left child of the node
#__________________________________________________________________________________________________________________________________________________
    def search(self, value):
        """
        search for a node with a specific value
        """
        node = self.root # start searching from the root of the tree
        while node != self.null_node: # continue searching until the current node is the null node/ leaf
            if value == node.value: # if the value of the current node is the value we are looking for then
                return node         # return the current node
            elif value < node.value: # if the value we are looking for is smaller than the value of the current node then
                node = node.left_child # go to the left child of the current node
            else:
                node = node.right_child # else go to the right child of the current node
        return None # if the value is not found in the tree then return None/ null
#__________________________________________________________________________________________________________________________________________________  
    def fix_RBtree(self,node):
        """
        the while loop is made to fix the RBTree properties
        """
        # if the parent of the node is red then there is a violation
        while node.parent.color == RED: # continue fixing the tree until the parent of the current node is black
            """
            If the parent of the current node is 
            the "left child" of its grandparent:

            Case 1- If the uncle of the current node is red: 

             -recolor the parent, uncle, and grandparent nodes and 
             continue fixing the tree from the grandparent.

            Case 2- If the uncle of the current node is black 
            and the current node is the right child of its parent:

             1-rotate the tree left to make the current node the left child 
             of its parent. 

             2-recolor the parent and grandparent nodes and rotate 
             the tree right to balance the tree.

            If the parent of the current node is
            the "right child" of its grandparent:

            Case 3- If the uncle of the current node is red:
             -recolor the parent, uncle, and grandparent nodes and continue 
             fixing the tree from the grandparent.

            Case 4- If the uncle of the current node is black 
            and the current node is the left child of its parent:
             
             1-rotate the tree right to make the current node the right child of its parent.
             2-recolor the parent and grandparent nodes and rotate the tree left to balance.
            """

            # CASE 1,2 - if the parent of the current node is the "left child" of its grandparent(uncle is the right child)
            if node.parent == node.parent.parent.left_child:
                uncle_node=node.parent.parent.right_child # the uncle of the current node is the right child of its grandparent
                """
                CASE 1
                if the uncle of the current node is red
                -recolor the parent, uncle, and grandparent nodes
                and continue fixing the tree from the grandparent
                """
                if uncle_node.color == RED: # if the uncle of the current node is red
                    node.parent.color = BLACK
                    uncle_node.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent # continue fixing the tree from the grandparent 
                    #(the grandparent is now the current node and the while loop will continue)
                else:
                    """
                    CASE 2
                    if the uncle of the current node is black
                    and the current node is the right child of its parent
                    1-rotate the tree left to make the current node the left child of its parent
                    2-recolor the parent and grandparent nodes and rotate the tree right to balance
                    """
                    # 1-rotate the tree left to make the current node the left child of its parent (same line)
                    if node == node.parent.right_child: # the current node is black and on the right side of its parent
                        node = node.parent
                        self.rotate_left(node) 
                    
                    # now the current node, parent and grand parent are in one line(left)
                    # 2-recolor the parent and grandparent nodes and rotate the tree right to balance
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.rotate_right(node.parent.parent) # rotate the tree right from the grandparent to balance the tree


            # CASE 3,4 - if the parent of the current node is the "right child" of its grandparent(uncle is the left child)
            else:
                uncle_node=node.parent.parent.left_child
                """
                CASE 3
                if the uncle of the current node is red
                -recolor the parent, uncle, and grandparent nodes
                and continue fixing the tree from the grandparent
                """
                if uncle_node.color == RED:
                    node.parent.color = BLACK
                    uncle_node.color = BLACK
                    node.parent.parent.color = RED
                    node = node.parent.parent
                else:
                    """
                    CASE 4
                    if the uncle of the current node is black
                    and the current node is the left child of its parent
                    1-rotate the tree right to make the current node the right child of its parent
                    2-recolor the parent and grandparent nodes and rotate the tree left to balance
                    """
                    # 1-rotate the tree right to make the current node the right child of its parent (same line)
                    if node == node.parent.left_child:
                        node = node.parent
                        self.rotate_right(node)
                    
                    # now the current node, parent and grand parent are in one line(right)
                    # 2-recolor the parent and grandparent nodes and rotate the tree left to balance
                    node.parent.color = BLACK
                    node.parent.parent.color = RED
                    self.rotate_left(node.parent.parent)
        """
        after the while loop finishes, the current node should be the root of the tree
        """
        node.color = BLACK # the root of the tree is always black
#__________________________________________________________________________________________________________________________________________________
    def print_height(self):
        """
        Print the height of the Red-Black tree. This is the longest path from the root to a leaf-node.
        """
        def get_height(node):
            if node == self.null_node: # if the current node is the null node then the height is 0(empty tree)
                return 0
            left_height = get_height(node.left_child) # get the height of the left subtree
            right_height = get_height(node.right_child) # get the height of the right subtree
            return 1 + max(left_height, right_height) # return the height of the tree as 1 + the height of the longest subtree (left or right)

        print("Tree height: ", get_height(self.root))
#__________________________________________________________________________________________________________________________________________________
    def print_size(self):
        """
        Print the number of elements in Red-Black tree.
        """
        print("Tree size: ", self.size)
#__________________________________________________________________________________________________________________________________________________