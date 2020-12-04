#Naomi Ighodaro
#Implements a simple Binary Tree
#Also implements the Binary Search algorith for the binary tree
#along with code to insert new elements.  

class BST:
  """Binary search tree based on 'BTNode's."""
  __slots__ = 'root'

  #-------------------------- nested BTNode class --------------------------
  class _BTNode:
    """ Lightweight, nonpublic class for storing a BTNode. """
    __slots__ = 'element', 'left', 'right'

    def __init__(self, element, left = None, right = None):
      self.element = element
      self.left    = left
      self.right   = right

    def hasLeft(self):
      """ Returns whether this node has a left child. """
      return self.left != None

    def hasRight(self):
      """ Returns whether this node has a right child. """
      return self.right != None

    def __lt__(self, other):
      """ Return True if other is a BTNode and this node is less than other. """
      return type(other) is type(self) and self.element < other.element

    def __gt__(self, other):
      """ Return True if other is a BTNode and this node is greater than other. """
      return type(other) is type(self) and self.element > other.element

    def __eq__(self, other):
      """ Return True if other is a BTNode and this node is equal to the other. """
      return type(other) is type(self) and self.element == other.element

  #-- c'tor
  def __init__(self):
    self.root = None


  #-- Public methods
  def insert(self, element):
    """ Insert element into the BST, keeping the BST property. """
    def _insertNode(root, node):
      if root == None or root == node:    # Overwrite if already present
        root = node
      else:
        if node < root:  # Go left
          if root.hasLeft():
            _insertNode(root.left, node)
          else:
            root.left = node
        else:            # Go right
          if root.hasRight():
            _insertNode(root.right, node)
          else:
            root.right = node

    # Create node to insert
    node = self._BTNode(element)

    if self.root == None:   # Special case for when tree is empty
      self.root = node
    else:
      _insertNode(self.root, node)


  def print(self):
    """ Print tree using inorder traversal. """
    def _print(root):
      if root != None:
        _print(root.left)
        print(root.element, end=' ')
        _print(root.right)

    _print(self.root)
    print();


#-- Main method
#creates a BST keeping BST property
tree = BST()
tree.insert(3)
tree.insert(1)
tree.insert(2)

tree.print()
