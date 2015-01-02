from ex2_1 import *

def make_ll(data):

	linky = LinkedList()

	for datum in data:
		linky.add_node(datum)

	return linky

def print_ll(linky):
	node = linky.head
	while node:
		print node.val,
		node = node.next
	print '\n'

if __name__ == '__main__':

	data = [2,7,8,3,5,7,8,9,3,5,7,6,4,2,6,5,8,4,7,5,0]

	linky = make_ll(data)

	print "linky with dupes:"
	print_ll(linky)

	#linky.remove_dupes_w_dict()
	linky.remove_dupes_no_dict()

	print "linky dupes removed:"
	print_ll(linky)


	
