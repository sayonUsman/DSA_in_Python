class LinearSearch:
	def __init__(self, List, search_num):
		self.List = List
		self.search_num = search_num
		
	def linear_search(self):
		for index in range(len(self.List)):
			if self.List[index] is self.search_num:
				return index
		else:
			return None
			
numbers = list(map(int, input("Please enter the sorted list of number: ").split()))
search_number = int(input("Please enter the search number: "))
linearSearch = LinearSearch(numbers, search_number)
index = linearSearch.linear_search()

if index is None:
	print("The search number does not exit in the list.")
else:
	print("The index of search number is", index)
	