#username - nc7
#id1      - 209223114
#name1    - noa cohen
#id2      - 205882236
#name2    - eyal cohen



"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields.

	@type value: str
	@param value: data of your node
	"""

	def __init__(self, value):
		self.value = value
		self.left = fakeNode
		self.right = fakeNode
		self.parent = None
		self.height = -1
		self.size = 1

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""

	def getLeft(self):
		return self.left

	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""

	def getRight(self):
		return self.right

	"""returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""

	def getParent(self):
		return self.parent

	"""returns the size 

	@rtype: AVLNode
	@returns: the size of self, 0 if the node is virtual
	"""
	def getSize(self):
		if self.isRealNode():
			return 0
		return self.size


	"""return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""

	def getValue(self):
		return self.value

	"""returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""

	def getHeight(self):
		return self.height

	"""sets left child

	@type node: AVLNode
	@param node: a node
	"""

	def setLeft(self, node):
		self.left = node

	"""sets right child

	@type node: AVLNode
	@param node: a node
	"""

	def setRight(self, node):
		self.right = node

	"""sets parent

	@type node: AVLNode
	@param node: a node
	"""

	def setParent(self, node):
		self.parent = node

	"""sets value

	@type value: str
	@param value: data
	"""

	def setValue(self, value):
		self.value = value

	"""sets the balance factor of the node

	@type h: int
	@param h: the height
	"""

	def setHeight(self, h):
		self.height = h

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def isRealNode(self):
		return self.height == -1



"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

	"""
	Constructor, you are allowed to add more fields.  

	"""
	def __init__(self):
		self.root = None
		self.size = 0
		# add your fields here


	"""returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""
	def empty(self):
		if self.size == 0:
			return True
		return False




	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""
	def retrieve(self, i):
		if i > self.size - 1 or i < 0 :
			return None
		return retriveRec(i,self.root)


	def retrieveRec(i,node):
		if node.left.getSize()  == i:
			return node.value
		elif node.left.getSize() < i:
			return retrievRec(i - node.left.getSize() - 1, node.right)
		elif node.left.getSize() > i:
			return retrievRec(i,node.left)





	"""inserts val at position i in the list

	@type i: int
	@pre: 0 <= i <= self.length()
	@param i: The intended index in the list to which we insert val
	@type val: str
	@param val: the value we inserts
	@rtype: list
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def insert(self, i, val):
		return -1


	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		return -1


	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""
	def first(self):
		if self.empty():
			return None
		node = self.root
		while node.left.isRealNode():
			node = node.left
		return node.value

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""
	def last(self):
		if self.empty():
			return None
		node = self.root
		while node.right.isRealNode():
			node = node.right
		return Node.value

	"""performs an inOrder scan using an action on all nodes by scan order
	
	@type node: AVLNode
	@param val: current node searched from
	@type action: function
	@param val: function to call on all nodes by order
	
	"""

	def inOrder(self, node, action):
		if node is None or not node.isRealNode():
			return
		self.inOrder(node.getLeft(), action)
		action(node)
		self.inOrder(node.getRight(), action)
		return

	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""

	def listToArray(self):
		result = []

		insertToResult = lambda node: result.append(node.getValue())

		self.inOrder(self.root, insertToResult)
		return result

	"""returns the size of the list 

	@rtype: int
	@returns: the size of the list
	"""
	def length(self):
		return self.size

	"""retrieves the node of the i'th item in the list

		@type i: int
		@pre: 0 <= i < self.length()
		@param i: index in the list
		@rtype: AVLNode
		@returns: the node of the i'th item in the list
		"""

	def retrieveNode(self, i):
		# todo modify retrieve to use this and extract value
		return fakeNode

	"""splits the list at the i'th index

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list according to whom we split
	@rtype: list
	@returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
	right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
	"""
	def split(self, i):
		node = self.retrieveNode(self, i)
		if node is None or not node.isRealNode():
			return [None, None, None]

		val = node.getValue()
		if self.root is None or not self.root.isRealNode():
			return [None, val, None]

		left_subtree = node.getLeft()
		right_subtree = node.getRight()
		parent = node.getParent()

		while parent is not None and parent.isRealNode():
			if parent.getRight() == node:
				left_subtree = self.join(parent.getLeft(), parent, left_subtree)
			else:
				right_subtree = self.join(right_subtree, parent, parent.getRight())

			node = parent
			parent = parent.getParent()

		return [left_subtree, val, node.getValue()]

	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def concat(self, lst):
		node_to_join = self.last()
		height_diff = abs(self.root.getHeight() - lst.root.getHeight())
		self.delete(self.size-1)  # size-1 is the index of last
		self.join(self.root, node_to_join, lst)

		return height_diff

	"""joins lst1 to lst 2 with node as the root

	@type lst1,lst2: AVLTreeList
	@param lst1,lst2: lists to be joined
	@type node: AVLNode
	@param node: node to connect between trees
	@rtype: AVLTreeList
	@returns: the joined lst
	"""
	def join(self, lst1, node, lst2):
		if lst1 is None or not lst1.root.isRealNode():
			lst2.insert(0, node.getValue())
			return lst2

		if lst2 is None or not lst2.root.isRealNode():
			lst1.insert((lst1.size-1), node.getValue())
			return lst1

		left_height = lst1.root.getHeight()
		right_height = lst2.root.getHeight()

		if left_height <= right_height:
			joined_lst = self.joinTallerRight(lst2, lst1, node, left_height)
		else:
			joined_lst = self.joinTallerLeft(lst1, lst2, node, right_height)

		return joined_lst

	"""joins tall_lst and small_lst with node as the connector node, 
	whilst part of the taller tree will be the left subtree of node
	
	@precondition: tall_lst is taller than small lst
	@type tall_lst,small_lst: AVLTreeList
	@param tall_lst,small_lst: lists to be joined
	@type node: AVLNode
	@param node: node to connect between trees
	@rtype: AVLTreeList
	@returns: the joined lst
	"""
	def joinTallerLeft(self, tall_lst, small_lst, node, small_height):
		lower_son = tall_lst.findRightSubtreeByHeight(small_height)
		lower_parent = lower_son.getParent()
		node.setLeft(lower_son)
		node.setRight(small_lst.root)
		node.setParent(lower_parent)
		lower_parent.setRight(node)
		# todo make sure balanced
		return tall_lst

	"""joins tall_lst and small_lst with node as the connector node, 
	whilst part of the taller tree will be the right subtree of node

	@precondition: tall_lst is taller than small lst
	@type tall_lst,small_lst: AVLTreeList
	@param tall_lst,small_lst: lists to be joined
	@type node: AVLNode
	@param node: node to connect between trees
	@rtype: AVLTreeList
	@returns: the joined lst
	"""
	def joinTallerRight(self, tall_lst, small_lst, node, small_height):
		lower_son = tall_lst.findLeftSubtreeByHeight(small_height)
		lower_parent = lower_son.getParent()
		node.setLeft(small_lst.root)
		node.setRight(lower_son)
		node.setParent(lower_parent)
		lower_parent.setLeft(node)
		# todo make sure balanced
		return tall_lst

	"""searches for the first (in order) node that contains value

	@type val: str
	@param val: a value to be searched
	@type node: AVLNode
	@param val: current node searched from
	@rtype: (AVLNode, int) tuple
	@returns: the first node that contains val and its index, node is None if not found.
	"""

	def inOrderSearch(self, node, val):
		if node is None or not node.isRealNode():
			return None, 0
		left_return_node, count_left = self.inOrderSearch(node.getLeft(), val)
		if left_return_node is not None:
			return left_return_node, count_left
		if val == node.getValue():
			return node, count_left
		right_return_node, count_right = self.inOrderSearch(node.getRight(), val)
		return right_return_node, count_left + count_right + 1

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""

	def search(self, val):
		found, found_index = self.inOrderSearch(self.root, val)
		if found is None:
			return -1
		return found_index


	"""returns the root of the tree representing the list

	@rtype: AVLNode
	@returns: the root, None if the list is empty
	"""
	def getRoot(self):
		if self.size == 0:
			return None
		else:
			return self.root


fakeNode = AVLNode(None)
