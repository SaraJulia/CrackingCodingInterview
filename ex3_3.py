"""
Implement a data structure representing a set of stacks, so that when one stack
gets too big, a new stack is created. There should be:
- a push method, which adds a value to the last stack or creates a new stack
- a pop method, which returns the last value on the last stack
..... and as follow up:
- a pop_at_idx method, which returns the last value at a specific substack

A stack is basically a list, so each substack is represented by a list.
"""

class SetOfStacks():

	# initialize an empty list to be the set of stacks
	def __init__(self):
		self.stackset = []

	# add a substack to the set
	def make_new_stack(self, val):
		new_stack = [val]
		self.stackset.append(new_stack)

	# add a value to the set of stacks
	def push(self, val):

		if len(self.stackset) == 0:
			self.make_new_stack(val)

		else:
			current_stack = self.stackset[-1]

			# arbitrarily decided a stack is 'too big' when it is more than 10
			# items long
			if len(current_stack) == 10:
				self.make_new_stack(val)
			else:
				current_stack.append(val)

	# pop off the last value of the last stack
	def pop(self):
		return self.stackset[-1].pop()

	# pop off the last value of a specific substack
	def pop_at_idx(self, idx):
		return self.stackset[idx].pop()

	def print_me(self):
		for stack in self.stackset:
			print stack,

		print "\n"



