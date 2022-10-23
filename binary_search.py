class BinarySearch:
	def __init__(self, List, search_num):
		self.__List = List
		self.__left_index = 0
		self.__right_index = len(List) - 1
		self.__search_num = search_num
		
	def binary_search(self):
		while(self.__left_index <= self.__right_index):
			mid = self.__left_index + (self.__right_index - self.__left_index) // 2
			if self.__List[mid] == self.__search_num:
				return mid
			elif self.__List[mid] > self.__search_num:
				self.__right_index = mid - 1
			else:
				self.__left_index = mid + 1
				
	
numbers = list(map(int, input("Please enter the sorted list of number: ").split()))
search_number = int(input("Please enter the search number: "))
binarySearch = BinarySearch(numbers, search_number)
index = binarySearch.binary_search()

if index is None:
	print("The search number does not exit in the list.")
else:
	print("The index of search number is", index)
	