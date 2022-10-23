class BinarySearch:
	@staticmethod
	def binary_search(items, search_item):
		left_index = 0
		right_index = len(items) - 1
			
		while left_index <= right_index:		
			mid_index = (left_index + right_index)  // 2
			if items[mid_index] == search_item:		
				return mid_index		
			elif items[mid_index] < search_item:		
				left_index = mid_index + 1			
			else:			
				right_index = mid_index - 1				
		
			
numbers = list(map(int, input("Please enter the sorted list of number: ").split()))
search_number = int(input("Please enter the search number: "))
binarySearch = BinarySearch()
index = binarySearch.binary_search(numbers, search_number)

if index is None:
	print("The search number does not exit in the list.")
else:
	print("The index of search number is", index)
	