"""
Check if a linked list has duplicates and remove them.
"""


class Node:
	def __init__(self, val):
		self.val = val
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def add_node(self, val):

		this_node = Node(val)

		if not self.head:
			self.head = this_node
			self.tail = this_node

		else:
			self.tail.next = this_node
			self.tail = this_node

	def print_me(self):
		node = self.head
		while node:
			print node.val,
			node = node.next
		print '\n'

	def remove_dupes_w_dict(self):

		values = {}
		node = self.head

		while node != self.tail:

			# put the current node in the dictionary
			values[node.val] = 1

			# check if the next node is in the dictionary
			if values.get(node.next.val):

				# check if the next node is the tail, and then delete the tail
				# this is necessary because there is no self.tail.next.next
				if node.next == self.tail:
					self.tail = node
					self.tail.next = None

				else:
					node.next = node.next.next

				# if the next node has been deleted, do not advance the pointer
				continue	
			
			# if the next node is not a duplicate, advance the pointer
			node = node.next


	def remove_dupes_no_dict(self):
		
		# create two pointers
		node = self.head
		seeker = self.head.next

		while node! = self.tail:

			while seeker:

				if node.val != seeker.val:
					seeker = seeker.next

				else:
					seeker.next = seeker.next


