from ex3_3 import *

def make_stackset(data):

	stacksettled = SetOfStacks()

	for datum in data:
		stacksettled.push(datum)

	return stacksettled



if __name__ == '__main__':

	data = range(51)

	stacksettled = make_stackset(data)
	stacksettled.print_me()

	print "popped off (should be 50): ", stacksettled.pop()
	stacksettled.print_me()
	print "\npopped off stack at idx 2 (should be 29): ", stacksettled.pop_at_idx(2)
	stacksettled.print_me()


