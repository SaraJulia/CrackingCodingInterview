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
			
			# if the next node is not a duplicate, advance the pointer
			else: 
				node = node.next


	def remove_dupes_no_dict(self):
		
		# create two pointers
		node = self.head
		seeker = self.head

		# loop the first pointer over the list
		while node:

			# loop the second pointer over the list
			while seeker != self.tail:

				# check if the value after the seeker is a duplicate, and 
				# delete if so
				if seeker.next.val == node.val:

					# in case the tail is a duplicate
					if seeker.next == self.tail:
						self.tail = seeker
						self.tail.next = None

					else:
						seeker.next = seeker.next.next

				# if the next value is not a duplicate, advance the pointer
				else:
					seeker = seeker.next

			# advance the first pointer and reset the seeker
			node = node.next
			seeker = node


