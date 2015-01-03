from ex3_3 import *

def make_stackset(data):

	stacksettled = SetOfStacks()

	for datum in data:
		stacksettled.push(datum)

	return stacksettled



if __name__ == '__main__':

	data = [2,7,8,3,5,7,8,9,3,5,7,6,4,2,6,5,8,4,7,5,0,36,8,3,2,6,7,8,3,32,2,2,6,89,3,2,4,5,7,8,9,9,4,43,3,45,7,6,89,53,24]

	stacksettled = make_stackset(data)
	stacksettled.print_me()

	print "popped off (should be 24): ", stacksettled.pop()
	print "popped off stack at idx 2 (should be 32): ", stacksettled.pop_at_idx(2)

