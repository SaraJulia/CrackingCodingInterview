"""
Implement a method to determine if a binary tree is balanced.
A binary tree is balanced when each subtree differs in height by at most one.
"""

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

	def has_children(self):
		if self.left or self.right:
			return True
		else:
			return False

class bTree:
	def __init__(self):
		self.root = None

	def add_node(self, val):

		new_node = Node(val)

		if not self.root:
			self.root = new_node

		else:
			node = self.root

			while node:
				if new_node.val > node.val:
					if node.right:
						node = node.right
					else:
						node.right = new_node
						return

				elif new_node.val < node.val:
					if node.left:
						node = node.left
					else:
						node.left = new_node
						return

				else:
					return "already exists"

	def get_height(self, node):
		if not node:
			return 0

		else:
			return max(self.get_height(node.left),
						self.get_height(node.right)) + 1


	def is_balanced(self, node):

		r_height = self.get_height(node.right)
		l_height = self.get_height(node.left)
		bal_factor = abs(r_height - l_height)

		return bal_factor <= 1

	def bft(self):

		queue = []

		node = self.root
		print node.val
		if node.left:
			queue.append(node.left)
		if node.right:
			queue.append(node.right)

		while queue:
			node = queue.pop(0)
			print node.val
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)





