class BubbleSort:
	def __init__(self, list):
		self.__list = list
		
	def swap(self, index, index2):
		temp = self.__list[index]
		self.__list[index]= self.__list[index2]
		self.__list[index2] = temp
		
	def bubble_sort(self):
		for index in range(len(self.__list) - 1):
			is_sorted = True
			for index2 in range(1, len(self.__list) - index):
				if self.__list[index2] < self.__list[index2 - 1]:
					self.swap(index2 - 1, index2)
					is_sorted = False
			if is_sorted:
				return 


numbers = list(map(int, input("Please enter the list of number: ").split()))
bubbleSort = BubbleSort(numbers)
bubbleSort.bubble_sort()
print(numbers)
