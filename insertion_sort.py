class InsertionSort:
	def __init__(self, list):
		self.__list = list
		
	def insertion_sort(self):
		for index in range(1, len(self.__list)):
			current = self.__list[index]
			index2 = index - 1
			while index2 >= 0 and self.__list[index2] > current:
				self.__list[index2 + 1] = self.__list[index2]
				index2 -= 1			
			self.__list[index2 + 1] = current 


numbers = list(map(int, input("Please enter the list of number: ").split()))
insertionSort = InsertionSort(numbers)
insertionSort.insertion_sort()
print(numbers)
