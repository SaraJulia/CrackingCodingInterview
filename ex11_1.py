"""
Given two sorted lists A and B, merge them into a sorted list.
"""

def merge_lists(list_A, list_B):

	# create two pointers, one for list A and B
	a = 0
	b = 0

	# loop over the lists, advancing the pointers each iteration
	while a < len(list_A) and b < len(list_B):

		if list_A[a] < list_B[b]:
			# do nothing, 'keep' element from A, but advance the pointer
			a += 1
			continue

		elif list_A[a] > list_B[b]:
			# insert the element from B into A, and advance both pointers
			list_A.insert(list_B[b], a)
			a += 1
			b += 1

	# if there's anything left in B, tack it on to A
	if b < len(list_B):
		list_A.extend(list_B[b:])


	# it's a bit easier to do this by creating another list and adding to it,
	# but I wanted to see if I could reduce memory requirements.
	return list_A

def main():

	print merge_lists([0,3,4,7,9], [1,2,5,6])

	print merge_lists([1,2,5,6], [0,3,4,7,9])

if __name__ == "__main__":
	main()