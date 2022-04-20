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
		if value == None:
			self.value = value
			self.height = -1
			self.size = 0
		else:
			self.value = value
			self.left = fakeNode
			self.right = fakeNode
			self.parent = None
			self.height = 0
			self.bf = 0
			self.size = 1

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""

	def getLeft(self):
		return None  # todo: after forum answer

	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""

	def getRight(self):
		return None  # todo: after forum answer

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
		if not self.isRealNode():
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
		if self.height == -1:
			return False
		return True

	def getbf(self):
		return self.bf



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
		return self.retrieveRec(i,self.root)


	def retrieveRec(self, i, node):
		if node.left.getSize()  == i:
			return node.value
		elif node.left.getSize() < i:
			return self.retrieveRec(i - node.left.getSize() - 1, node.right)
		elif node.left.getSize() > i:
			return self.retrieveRec(i,node.left)





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
		newNode = AVLNode(val)
		if self.root == None:
			self.root = newNode
			self.size += 1
		elif i == self.size:
			node = self.root
			while node.right.isRealNode():
				node = node.right
			node.right = newNode
			newNode.parent = node
			x = self.fixbfInsert(node)
			self.fixNodesSizeInsert(node)
			self.size += 1
			return x
		else:
			optionalNode = self.retrieveRecNode(i, self.root)
			if not optionalNode.left.isRealNode():
				optionalNode.left = newNode
				newNode.parent = optionalNode
				x = self.fixbfInsert(optionalNode)
				self.fixNodesSizeInsert(optionalNode)
				self.size += 1
				return x
			else:
				optionalNode = self.find_predecessor(optionalNode)
				optionalNode.right = newNode
				newNode.parent = optionalNode
				x = self.fixbfInsert(optionalNode)
				self.fixNodesSizeInsert(optionalNode)
				self.size += 1
				return x


	def fixNodesSizeInsert(self,node):
		while node != None:
			node.size += 1
			node = node.parent
		return None

	def fixbfInsert(self, node):
		counter = 0
		while node != None:
			node.bf = node.left.getHeight() - node.right.getHeight()
			if node.getHeight() == max(node.right.getHeight(),node.left.getHeight()) + 1 and abs(node.getbf()) < 2: #assuming new node (leaf) height = 0, meaning node height didn't change
				break
			elif abs(node.getbf()) < 2 : #node's height has changed but rotation not needed
				node.setHeight(max(node.right.getHeight(), node.left.getHeight()) + 1)
				counter += 1
			elif abs(node.bf) > 1: #rotaion is needed
				r = self.checkRotationNeeded(node)
				if r == 1: #left rotation
					counter += 1
					if node == self.root:
						self.root = self.leftrotation(node)
					else:
						x = node.parent
						y = self.leftrotation(node)
						x.right = y
						y.parent = x
					return counter
				elif r == 2: #rl rotation
					counter += 2
					node.right = self.rightrotaion(node.right)
					if node == self.root:
						self.root = self.leftrotation(node)
					else:
						x = node.parent
						x.right = self.leftrotation(node)
						x.right.parent = x
					return counter
				elif r == 3: #right rotation
					counter += 1
					if node == self.root:
						self.root = self.rightrotaion(node)
						self.root.setParent(None)
					else:
						x = node.parent
						y = self.rightrotaion(node)
						x.left = y
						y.parent = x
					return counter
				elif r == 4: #lr rotation
					counter += 2
					node.left = self.leftrotation(node.left)
					if node == self.root:
						self.root = self.rightrotaion(node)
					else:
						x = node.parent
						x.left = self.rightrotaion(node)
						x.left.parent = x
					return counter
			node = node.parent
		return counter

	def checkRotationNeeded(self, node):
		if node.right.isRealNode():
			if node.bf == -2 and node.right.bf == -1:
				return 1 #left rotation
			elif node.bf == -2 and node.right.bf == 1:
				return 2 #right and than left rotation
		if node.left.isRealNode():
			if node.bf == 2 and node.left.bf == 1:
				return 3 #right rotation
			elif node.bf == 2 and node.left.bf == -1:
				return 4 #left and than right roataion

	def rightrotaion(self,z):
		y = z.left
		t3 = y.right
		y.right = z
		y.parent = z.parent
		z.parent = y
		z.left = t3
		t3.parent = z
		z.height = max(z.left.getHeight(), z.right.getHeight()) + 1
		y.height = max(y.left.getHeight(), y.right.getHeight()) + 1
		y.size = z.size
		z.size = z.right.size + z.left.size + 1
		return y

	def leftrotation(self,z):
		y = z.right
		t2 = y.left
		y.left = z
		y.parent = z.parent
		z.parent = y
		z.right = t2
		t2.parent = z
		z.height = max(z.left.getHeight(), z.right.getHeight()) + 1
		y.height = max(y.left.getHeight(), y.right.getHeight()) + 1
		y.size = z.size
		z.size = z.right.size + z.left.size + 1
		return y

	def retrieveRecNode(self, i, node):
		if node.left.getSize()  == i:
			return node
		elif node.left.getSize() < i:
			return self.retrieveRecNode(i - node.left.getSize() - 1, node.right)
		elif node.left.getSize() > i:
			return self.retrieveRecNode(i,node.left)

	def find_predecessor(self, node):
		node = node.left
		while node.right.isRealNode():
			node = node.right
		return node








	"""deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, i):
		if i > self.size - 1:
			return -1
		nodeTodelete = self.retrieveRecNode(i , self.root)
		if nodeTodelete.left.isRealNode() and nodeTodelete.right.isRealNode(): #node has 2 boys
			successorNode = self.find_successor(nodeTodelete)
			nodeTodelete.value = successorNode.value
			if successorNode.right.isRealNode():
				if successorNode.parent.right == successorNode:
					x = successorNode.parent
					successorNode.parent.setRight(successorNode.right)
					successorNode.right.setParent(successorNode.parent)
				else:
					x = successorNode.parent
					x.setLeft(successorNode.right)
					successorNode.right.setParent(x)
				successorNode.setParent(None)
				successorNode.setRight(None)
				self.fixNodesSizeDelete(x)
				res = self.fixbfDelete(x)
				self.size -= 1
				return res
			else:
				if successorNode.parent.right == successorNode: #seccessor node is right to deleted node
					x = successorNode.parent
					successorNode.parent.setRight(fakeNode)
					successorNode.setParent(None)
				else: #seccessor node is left boy
					x = successorNode.parent
					successorNode.parent.setLeft(fakeNode)
					successorNode.setParent(None)
				self.fixNodesSizeDelete(x)
				res = self.fixbfDelete(x)
				self.size -= 1
				return res
		elif nodeTodelete.left.isRealNode() and not nodeTodelete.right.isRealNode(): #node has only left boy
			x = nodeTodelete.parent
			if x.left == nodeTodelete:
				nodeTodelete.left.setParent(nodeTodelete.parent)
				nodeTodelete.parent.setLeft(nodeTodelete.left)
			elif x.right == nodeTodelete:
				nodeTodelete.left.setParent(nodeTodelete.parent)
				nodeTodelete.parent.setRight(nodeTodelete.left)
			nodeTodelete.setParent(None)
			nodeTodelete.setLeft(None)
			self.fixNodesSizeDelete(x)
			res = self.fixbfDelete(x)
			self.size -= 1
			return res
		elif not nodeTodelete.left.isRealNode() and nodeTodelete.right.isRealNode(): #node has only right boy
			x = nodeTodelete.parent
			if x.left == nodeTodelete:
				nodeTodelete.right.setParent(nodeTodelete.parent)
				nodeTodelete.parent.setLeft(nodeTodelete.right)
			elif x.right == nodeTodelete:
				nodeTodelete.right.setParent(nodeTodelete.parent)
				nodeTodelete.parent.setRight(nodeTodelete.right)
			nodeTodelete.setParent(None)
			nodeTodelete.setRight(None)
			self.fixNodesSizeDelete(x)
			res = self.fixbfDelete(x)
			self.size -= 1
			return res
		elif not nodeTodelete.left.isRealNode() and not nodeTodelete.right.isRealNode(): #node is a leaf
			x = nodeTodelete.parent
			if nodeTodelete.parent.right == nodeTodelete: #leaf is a right son
				nodeTodelete.parent.setRight(fakeNode)
				nodeTodelete.setParent(None)
			else: #leaf is a left son
				nodeTodelete.parent.setLeft(fakeNode)
				nodeTodelete.setParent(None)
			self.fixNodesSizeDelete(x)
			res = self.fixbfDelete(x)
			self.size -= 1
			return res




	def fixbfDelete(self, node):
		counter = 0
		while node != None:
			node.bf = node.left.getHeight() - node.right.getHeight()
			if node.getHeight() == max(node.right.getHeight(), node.left.getHeight()) + 1 and abs(node.getbf()) < 2:  # assuming new node (leaf) height = 0, meaning node height didn't change
				break
			elif abs(node.getbf()) < 2:  # node's height has changed but rotation not needed
				node.setHeight(max(node.right.getHeight(), node.left.getHeight()) + 1)
				counter += 1
			elif abs(node.bf) > 1:  # rotaion is needed
				r = self.checkRotationNeededDeletion(node)
				if r == 1:  # left rotation
					counter += 1
					if node == self.root:
						self.root = self.leftrotation(node)
						self.root.setParent(None)
						node = node.parent
					elif node.parent.left == node:
						x = node.parent
						y = self.leftrotation(node)
						x.left = y
						y.parent = x
						node = y.parent
					else:
						x = node.parent
						y = self.leftrotation(node)
						x.right = y
						y.parent = x
						node = y.parent
				elif r == 2:  # rl rotation
					counter += 2
					node.right = self.rightrotaion(node.right)
					if node == self.root:
						self.root = self.leftrotation(node)
						self.root.setParent(None)
						node = node.parent
					elif node.parent.left == node:
						x = node.parent
						x.left = self.leftrotation(node)
						x.left.parent = x
						node = x
					else:
						x = node.parent
						x.right = self.leftrotation(node)
						x.right.parent = x
						node = x
				elif r == 3:  # right rotation
					counter += 1
					if node == self.root:
						self.root = self.rightrotaion(node)
						self.root.setParent(None)
						node = node.parent
					elif node.parent.left == node:
						x = node.parent
						y = self.rightrotaion(node)
						x.left = y
						y.parent = x
						node = y.parent#####
					else:
						x = node.parent
						y = self.rightrotaion(node)
						x.right = y
						y.parent = x
						node = y.parent#####
				elif r == 4:  # lr rotation
					counter += 2
					node.left = self.leftrotation(node.left)
					if node == self.root:
						self.root = self.rightrotaion(node)
						node = node.parent ######
					elif node.parent.right == node:
						x = node.parent
						x.right = self.rightrotaion(node)
						x.right.parent = x
						node = x
					else:
						x = node.parent
						x.left = self.rightrotaion(node)
						x.left.parent = x
						node = x
		return counter

	def checkRotationNeededDeletion(self, node):
		if node.right.isRealNode():
			node.right.bf = node.right.left.getHeight() - node.right.right.getHeight()
			if node.bf == -2 and (node.right.bf == -1 or node.right.bf == 0):
				return 1 #left rotation
			elif node.bf == -2 and node.right.bf == 1:
				return 2 #right and than left rotation
		if node.left.isRealNode():
			node.left.bf = node.left.left.getHeight() - node.left.right.getHeight()
			if node.bf == 2 and (node.left.bf == 1 or node.left.bf == 0):
				return 3 #right rotation
			elif node.bf == 2 and node.left.bf == -1:
				return 4 #left and than right roataion

	def fixNodesSizeDelete(self,node):
		while node != None:
			node.size -= 1
			node = node.parent
		return None


	def find_successor(self, node):
		node = node.right
		while node.left.isRealNode():
			node = node.left
		return node


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
		return node.value

	"""returns an array representing list 

	@rtype: list
	@returns: a list of strings representing the data structure
	"""

	def inOrder(self, node, action):
		if node is None or not node.isRealNode():
			return
		self.inOrder(node.getLeft(), action)
		action(node)
		self.inOrder(node.getRight(), action)
		return

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

	"""splits the list at the i'th index

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list according to whom we split
	@rtype: list
	@returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
	right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
	"""
	def split(self, i):
		return None

	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""
	def concat(self, lst):
		return None

	"""searches for a *value* in the list

	@type val: str
	@param val: a value to be searched
	@rtype: int
	@returns: the first index that contains val, -1 if not found.
	"""
	def search(self, val):
		return None



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
