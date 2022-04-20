# username - nc7
# id1      - 209223114
# name1    - noa cohen
# id2      - 205882236
# name2    - eyal cohen

# todo later when we have time:
# documentations
# not sure if we need to save bf cause we are calculating it by height - ask eyal

"""A class represnting a node in an AVL tree"""


class AVLNode(object):
	"""Constructor, you are allowed to add more fields.

	@type value: str
	@param value: data of your node
	"""
	fakeNode = None

	def __init__(self, value):
		self.value = value
		self.left = self.fakeNode
		self.right = self.fakeNode
		self.parent = None
		self.height = -1
		self.bf = 0
		self.size = 1

	"""returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""

	def getLeft(self):
		if not self.isRealNode():
			return None
		return self.left

	"""returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""

	def getRight(self):
		if not self.isRealNode():
			return None
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

	"""returns the balance factor

		@rtype: int
		@returns: the balance factor of self
	"""

	def getBF(self):
		return self.bf

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

	"""sets the height of the node

	@type h: int
	@param h: the height
	"""

	def setHeight(self, h):
		self.height = h

	"""sets the balance factor of the node

	@type bf: int
	@param bf: the height
	"""

	def setBF(self, bf):
		self.bf = bf

	"""sets the size of the node

	@type s: int
	@param s: the size
	"""

	def setSize(self, s):
		self.size = s

	"""
	increases the node size by i
	
	@type i: int
	@param i: number to increase by (or decrease if negative num)
	"""

	def increaseSizeBy(self, i):
		self.size = self.size + i

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""

	def isRealNode(self):
		return self.height != -1


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
		return self.size == 0

	"""retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""

	def retrieve(self, i):
		if i > self.size - 1 or i < 0 or self.empty():
			return None
		node = self.retrieveRec(i, self.root)
		if node is None:
			return None
		return node.getValue()

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
		new_node = AVLNode(val)
		new_node.setHeight(0)
		self.size += 1

		if self.root is None:
			self.root = new_node
			return 0
		elif i == self.size-1:
			node = self.root
			while node.getRight().isRealNode():
				node = node.getRight()
			node.setRight(new_node)
			return self.setParentAndRebalance(new_node, node)
		else:
			optional_parent_node = self.retrieveNode(i)
			if not optional_parent_node.getLeft().isRealNode():
				optional_parent_node.setLeft(new_node)
				return self.setParentAndRebalance(new_node, optional_parent_node)
			else:
				optional_parent_node = self.find_predecessor(optional_parent_node)
				optional_parent_node.setRight(new_node)
				return self.setParentAndRebalance(new_node, optional_parent_node)

	# todo documentation
	def setParentAndRebalance(self, new_node, optional_parent_node):
		new_node.setParent(optional_parent_node)
		num_rebalance_op = self.fixbf(optional_parent_node)
		if new_node.getParent() != optional_parent_node:
			optional_parent_node = new_node
		self.fixNodesSize(optional_parent_node, 1)
		return num_rebalance_op

	def fixbf(self, node, stopAfterRotate=True, forDelete=False):
		counter = 0
		while node is not None:
			left_height = node.getLeft().getHeight()
			right_height = node.getRight().getHeight()
			node.setBF(left_height - right_height)

			new_height = max(right_height, left_height) + 1
			# assuming new node (leaf) height = 0, meaning node height didn't change
			if node.getHeight() == new_height and abs(node.getBF()) < 2:
				break

			elif abs(node.getBF()) < 2:  # node's height has changed but rotation not needed
				node.setHeight(new_height)
				counter += 1

			# returning cause one rotation is enough in insert
			elif abs(node.getBF()) > 1:  # rotation is needed
				r = self.checkRotationNeeded(node, forDelete)
				if r == 1:  # left rotation
					counter = self.leftRotation(counter, node)
				elif r == 2:  # rl rotation
					counter = self.rightLeftRotation(counter, node)
				elif r == 3:  # right rotation
					counter = self.rightRotation(counter, node)
				elif r == 4:  # lr rotation
					counter = self.leftRightRotation(counter, node)
				if stopAfterRotate:
					return counter
			node = node.getParent()
		return counter

	# todo documentation
	def checkRotationNeeded(self, node, forDelete=False):
		right = node.getRight()
		left = node.getLeft()
		bf = node.getBF()
		if right.isRealNode():
			right_bf = right.getBF()
			if bf == -2 and (right_bf == -1 or (forDelete and right_bf == 0)):
				return 1  # left rotation
			elif bf == -2 and right_bf == 1:
				return 2  # right and than left rotation
		if left.isRealNode():
			left_bf = left.getBF()
			if bf == 2 and (left_bf == 1 or (forDelete and left_bf == 0)):
				return 3  # right rotation
			elif bf == 2 and left_bf == -1:
				return 4  # left and than right roataion

	# todo documentation
	def leftRightRotation(self, counter, node):
		counter += 2
		node.setLeft(self.rotateLeft(node.getLeft()))
		if node == self.root:
			self.root = self.rotateRight(node)
			return counter

		x = node.getParent()
		new_son = self.rotateRight(node)
		new_son.setParent(x)
		if x.getLeft() == node:
			x.setLeft(new_son)
		else:
			x.setRight(new_son)
		return counter

	# todo documentation
	def rightRotation(self, counter, node):
		counter += 1
		if node == self.root:
			self.root = self.rotateRight(node)
			self.root.setParent(None)
			return counter

		x = node.getParent()
		y = self.rotateRight(node)
		y.setParent(x)
		if x.getLeft() == node:
			x.setLeft(y)
		else:
			x.setRight(y)
		return counter

	# todo documentation
	def rightLeftRotation(self, counter, node):
		counter += 2
		node.setRight(self.rotateRight(node.getRight()))
		if node == self.root:
			self.root = self.rotateLeft(node)
			self.root.setParent(None)
			return counter

		x = node.getParent()
		new_son = self.rotateLeft(node)
		new_son.setParent(x)
		if x.getLeft() == node:
			x.setLeft(new_son)
		else:
			x.setRight(new_son)
		return counter

	# todo documentation
	def leftRotation(self, counter, node):
		counter += 1
		if node == self.root:
			self.root = self.rotateLeft(node)
			self.root.setParent(None)
			return counter
		parent = node.getParent()
		y = self.rotateLeft(node)
		y.setParent(parent)
		if parent.getLeft() == node:
			parent.setLeft(y)
		else:
			parent.setRight(y)
		return counter

	# todo documentation
	def rotateRight(self, z):
		y = z.getLeft()
		new_z_left = y.getRight()
		y.setRight(z)
		y.setParent(z.getParent())
		z.setParent(y)
		z.setLeft(new_z_left)
		new_z_left.setParent(z)
		z_new_height = max(new_z_left.getHeight(), z.getRight().getHeight()) + 1
		z.setHeight(z_new_height)
		y.setHeight(max(y.getLeft().getHeight(), z_new_height) + 1)
		y.setSize(z.getSize())
		z.setSize(z.getRight().getSize() + new_z_left.getSize() + 1)
		return y

	# todo documentation
	def rotateLeft(self, z):
		y = z.getRight()
		new_z_right = y.getLeft()
		y.setLeft(z)
		y.setParent(z.getParent())
		z.setParent(y)
		z.setRight(new_z_right)
		new_z_right.setParent(z)
		new_z_height = max(z.getLeft().getHeight(), new_z_right.getHeight()) + 1
		z.setHeight(new_z_height)
		y.height = max(new_z_height, y.getRight().getHeight()) + 1
		y.setSize(z.getSize())
		z.setSize(new_z_right.getSize() + z.getLeft().getSize() + 1)
		return y

	# todo documentation
	def find_predecessor(self, node):
		node = node.getLeft()
		while node.getRight().isRealNode():
			node = node.getRight()
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

		node_to_delete = self.retrieveNode(i)
		left = node_to_delete.getLeft()
		right = node_to_delete.getRight()

		if left.isRealNode() and right.isRealNode():  # node has 2 boys
			return self.deleteWithTwoSons(node_to_delete)

		elif left.isRealNode() and not right.isRealNode():  # node has only left boy
			num_rebalance = self.deleteWithOneSon(node_to_delete, left)
			node_to_delete.setLeft(None)
			return num_rebalance

		elif not left.isRealNode() and right.isRealNode():  # node has only right boy
			num_rebalance = self.deleteWithOneSon(node_to_delete, right)
			node_to_delete.setRight(None)
			return num_rebalance

		elif not node_to_delete.left.isRealNode() and not node_to_delete.right.isRealNode():  # node is a leaf
			return self.DeleteLeaf(node_to_delete)

	# todo add documentation
	def DeleteLeaf(self, node_to_delete):
		del_parent = node_to_delete.getParent()
		if del_parent is None:
			self.root = None
			self.size = 0
			return 0
		if del_parent.getRight() == node_to_delete:  # leaf is a right son
			del_parent.setRight(fakeNode)
		else:  # leaf is a left son
			del_parent.setLeft(fakeNode)
		node_to_delete.setParent(None)
		num_rebalance = self.rebalanceAndCount(del_parent)
		return num_rebalance

	# todo add documentation
	def deleteWithTwoSons(self, node_to_delete):
		successorNode = self.find_successor(node_to_delete)
		node_to_delete.setValue(successorNode.getValue())
		succ_right = successorNode.getRight()
		succ_parent = successorNode.getParent()
		if succ_right.isRealNode():
			succ_right.setParent(succ_parent)
			num_rebalance_op = self.deleteBySuccessor(succ_parent, succ_right, successorNode)
			successorNode.setRight(fakeNode)
		else:
			num_rebalance_op = self.deleteBySuccessor(succ_parent, fakeNode, successorNode)
		return num_rebalance_op

	# todo add documentation
	def deleteWithOneSon(self, node_to_delete, son):
		del_parent = node_to_delete.getParent()
		son.setParent(del_parent)
		if del_parent is None:
			self.root = son
		elif del_parent.getLeft() == node_to_delete:
			del_parent.setLeft(son)
		elif del_parent.getRight() == node_to_delete:
			del_parent.setRight(son)
		node_to_delete.setParent(None)
		num_rebalance = self.rebalanceAndCount(del_parent)
		return num_rebalance

	# todo add documentation
	def deleteBySuccessor(self, succ_parent, succ_right, successorNode):
		if succ_parent is None:
			pass
		elif succ_parent.getRight() == successorNode:
			succ_parent.setRight(succ_right)
		else:
			succ_parent.setLeft(succ_right)
		successorNode.setParent(None)
		return self.rebalanceAndCount(succ_parent)

	# todo add documentation
	def rebalanceAndCount(self, succ_parent):
		self.fixNodesSize(succ_parent, -1)
		num_rebalance_op = self.fixbf(succ_parent, False, True)
		self.size -= 1
		return num_rebalance_op

	# todo documentation
	def fixNodesSize(self, node, incrementBy):
		while node is not None:
			node.increaseSizeBy(incrementBy)
			node = node.getParent()

	# todo documentation
	def find_successor(self, node):
		node = node.getRight()
		while node.getLeft().isRealNode():
			node = node.getLeft()
		return node

	"""returns the value of the first item in the list

	@rtype: str
	@returns: the value of the first item, None if the list is empty
	"""

	def first(self):
		get_left = lambda node: node.getLeft()
		node = self.getTreeEdge(get_left)
		if node is None:
			return None
		return node.getValue()

	"""returns the value of the last item in the list

	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""

	def last(self):
		get_right = lambda node: node.getRight()
		node = self.getTreeEdge(get_right)
		if node is None:
			return None
		return node.getValue()


	"""returns the value of the item in the list that is in edge left or right
	
	@type getSide: lambda
	@param getSide: a function that returns left son or right son of node
	@rtype: str
	@returns: the value of the last item, None if the list is empty
	"""

	def getTreeEdge(self, getSide):
		if self.empty():
			return None
		node = self.root
		while getSide(node).isRealNode():
			node = getSide(node)
		return node

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
		if self.empty():
			return None
		return self.retrieveRec(i, self.root)

	"""retrieves the node of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@type node: AVLNode
	@param node: node current "root" of tree in recursion
	@rtype: AVLNode
	@returns: the node of the i'th item in the list
	"""

	def retrieveRec(self, i, node):
		if node is None or not node.isRealNode():
			return
		left_size = node.getLeft().getSize()
		if left_size == i:
			return node
		elif left_size < i:
			return self.retrieveRec(i - left_size - 1, node.getRight())
		else:
			return self.retrieveRec(i, node.getLeft())

	"""splits the list at the i'th index

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list according to whom we split
	@rtype: list
	@returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
	right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
	"""

	def split(self, i):
		node = self.retrieveNode(i)
		if node is None or not node.isRealNode():
			return [None, None, None]

		val = node.getValue()
		if self.root is None or not self.root.isRealNode():
			return [None, val, None]

		left_subtree_root = node.getLeft()
		right_subtree_root = node.getRight()
		left_subtree = self.createTreeListFromRoot(left_subtree_root)
		right_subtree = self.createTreeListFromRoot(right_subtree_root)
		parent = node.getParent()

		while parent is not None and parent.isRealNode():
			if parent.getRight() == node:
				new_left_sub = self.createTreeListFromRoot(parent.getLeft())
				left_subtree = self.join(new_left_sub, parent, left_subtree)
			else:
				new_right_sub = self.createTreeListFromRoot(parent.getRight())
				right_subtree = self.join(right_subtree, parent, new_right_sub)

			node = parent
			parent = parent.getParent()

		return [left_subtree, val, right_subtree]

	def createTreeListFromRoot(self, left_subtree_root):
		left_subtree = AVLTreeList()
		left_subtree.root = left_subtree_root
		left_subtree.size = left_subtree_root.getSize()
		return left_subtree

	"""concatenates lst to self

	@type lst: AVLTreeList
	@param lst: a list to be concatenated after self
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""

	def concat(self, lst):
		get_right = lambda node: node.getRight()
		node_to_join = self.getTreeEdge(get_right) # gets last node
		self_height, lst_height = 0, 0
		if self.root is not None:
			self_height = self.root.getHeight()
		if lst.root is not None:
			lst_height = lst.root.getHeight()
		height_diff = abs(self_height - lst_height)
		self.delete(self.size - 1)  # size-1 is the index of last
		joined = self.join(self, node_to_join, lst)
		self.root = joined.root
		self.size = joined.size

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
		if lst1 is None or lst1.root is None or not lst1.root.isRealNode():
			lst2.insert(0, node.getValue())
			return lst2

		if lst2 is None or lst2.root is None or not lst2.root.isRealNode():
			lst1.insert((lst1.size - 1), node.getValue())
			return lst1

		left_height = lst1.root.getHeight()
		right_height = lst2.root.getHeight()

		if left_height <= right_height:
			joined_lst = self.joinTallerRight(lst2, lst1, node, left_height)
		else:
			joined_lst = self.joinTallerLeft(lst1, lst2, node, right_height)

		joined_lst.size = lst1.size + lst2.size
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
		getRight = lambda n: n.getRight()
		lower_son = tall_lst.findSideSubtreeByHeight(small_height, getRight)
		lower_parent = lower_son.getParent()
		node.setLeft(lower_son)
		node.setRight(small_lst.root)
		node.setParent(lower_parent)
		if lower_parent is not None:
			lower_parent.setRight(node)
		else:
			lower_parent = node
		# todo make sure lower parent is the correct node
		self.fixbf(lower_parent, False, True)
		self.fixNodeFieldsJoin(lower_parent)
		return tall_lst

	def findSideSubtreeByHeight(self, height, getSide):
		node = self.root
		while node.getHeight() > height:
			node = getSide(node)
		return node

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
		getLeft = lambda n: n.getLeft()
		lower_son = tall_lst.findSideSubtreeByHeight(small_height, getLeft)
		lower_parent = lower_son.getParent()
		node.setLeft(small_lst.root)
		node.setRight(lower_son)
		node.setParent(lower_parent)
		if lower_parent is not None:
			lower_parent.setLeft(node)
		else:
			lower_parent = node
			tall_lst.root = node
		# todo make sure lower parent is the correct node
		self.fixbf(lower_parent, False, True)
		self.fixNodeFieldsJoin(lower_parent)
		return tall_lst

	def fixNodeFieldsJoin(self, node):
		while node is not None and node.isRealNode():
			left = node.getLeft()
			right = node.getRight()
			left_height, right_height = 0, 0
			new_size = 0
			if left is not None and left.isRealNode():
				left_height = left.getHeight()
				new_size += left.getSize()
			if right is not None and right.isRealNode():
				right_height = right.getHeight()
				new_size += right.getSize()
			new_height = max(left_height, right_height) + 1
			node.setHeight(new_height)
			node.setSize(new_size + 1)
			node = node.getParent()
		return


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

	# todo delete this
	def printt(self):
		out = ""
		for row in self.printree(self.root):  # need printree.py file
			out = out + row + "\n"
		print(out)

	def printree(self, t, bykey=True):
		# for row in trepr(t, bykey):
		#        print(row)
		return self.trepr(t, False)

	def trepr(self, t, bykey=False):
		if t == None:
			return ["#"]

		thistr = str(t.key) if bykey else str(t.getValue())

		return self.conc(self.trepr(t.left, bykey), thistr, self.trepr(t.right, bykey))

	def conc(self, left, root, right):

		lwid = len(left[-1])
		rwid = len(right[-1])
		rootwid = len(root)

		result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

		ls = self.leftspace(left[0])
		rs = self.rightspace(right[0])
		result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid *
					  " " + "\\" + rs * "_" + (rwid - rs) * " ")

		for i in range(max(len(left), len(right))):
			row = ""
			if i < len(left):
				row += left[i]
			else:
				row += lwid * " "

			row += (rootwid + 2) * " "

			if i < len(right):
				row += right[i]
			else:
				row += rwid * " "

			result.append(row)

		return result

	def leftspace(self, row):
		# row is the first row of a left node
		# returns the index of where the second whitespace starts
		i = len(row) - 1
		while row[i] == " ":
			i -= 1
		return i + 1

	def rightspace(self, row):
		# row is the first row of a right node
		# returns the index of where the first whitespace ends
		i = 0
		while row[i] == " ":
			i += 1
		return i

	def append(self, val):
		return self.insert(self.length(), val)

	def getTreeHeight(self):
		return self.root.getHeight()


AVLNode.fakeNode = AVLNode(None)
fakeNode = AVLNode.fakeNode
