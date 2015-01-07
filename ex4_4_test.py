from ex4_4 import *

def check_tree_balance(data):

	tree = bTree()

	for datum in data:
		tree.add_node(datum)

	# quick check to see if tree entered correctly
	#tree.bft()

	return tree.is_balanced(tree.root)


if __name__ == '__main__':
	balanced_data = [4, 2, 1, 0, 3, 8, 6, 7, 10, 9, 11, 12]
	unbalanced_data = range(13)

	#print "Balanced: ", check_tree_balance(balanced_data)
	#print "Unbalanced: ", check_tree_balance(unbalanced_data)

	print "Balanced: ", check_tree_balance(balanced_data)
	print "Unbalanced: ", check_tree_balance(unbalanced_data)

